import subprocess, os
from . import celery
from simulators import SIMULATORS
from flask_login import current_user
from app.models import Job
import arc

JOB_THRESHOLD = 6

@celery.task
def start_job(job_id):
    """
        This is the main function to be consumed by the celery instance.
        This must be well defined and flexible enough to handle a variety of
        jobs and parameters. The function will update the database if any errors occur.

        = Parameters =
        job_id       : string   = valid string that represents the job's database id

        = Return =
        boolean = the status of the job (true=success, false=failed)
            The cause of failure will will be written to the mongo database
    """

    job = Job.objects(id=job_id).first()
    if job == None:
        return 'no job found'

    job.status = 'queued'
    job.save()

    # Validate simulator
    sim_id = job.simulator
    if sim_id is None or sim_id not in SIMULATORS:
        job.status = 'failed'
        job.err = 'Invalid simulator or simulator does not exist'
        job.save()
        return 'invalid simulator'

    sim = SIMULATORS[sim_id]

    # Validate parameters.
    for arg in sim['arguments']:
        if arg == 'input' or arg == 'output':
            continue
        if arg not in job.attrs:
            job.status = 'failed'
            job.err = 'Missing argument: {}'.format(arg)
            job.save()
            return 'missing argument: {}'.format(arg)

    client = arc.Client('newriver1.arc.vt.edu', arc.ARC_USER)
    try:
        current_job_count = int(client.run('qstat | grep {} | wc -l'.format(arc.ARC_USER)))
        if current_job_count > JOB_THRESHOLD:
            submit_retry(job)
            client.close()
            return 'arc is full'
    except ValueError:
        submit_retry(job)
        client.close()
        return 'failed to check arc status'

    remote_path = arc.get_remote_path(arc.ARC_USER, job.id)
    input_path = os.path.join(remote_path, 'input.fasta')
    output_path = os.path.join(remote_path, 'output')

    qsub_path = os.path.join(arc.QSUB_DIR, '{}.qsub'.format(sim_id))
    arguments = [ str(job.id) ]

    for arg in sim['arguments']:
        if arg == 'input':
            arguments.append(input_path)
        elif arg == 'output':
            arguments.append(output_path)
        elif arg == 'extra_file':
            arguments.append(os.path.join(remote_path, 'extra_file'))
        else:
            arguments.append(str(job.attrs[arg]))

    client.run('qsub {} -F "{}"'.format(qsub_path, ' '.join(arguments)))
    client.close()

    job.status = 'submitted'
    job.save()
    return True

def create_and_start_job(sim_id, form, extra_file=None):
    job_attrs = dict()
    data = { 'simulator' : sim_id, 'status' : 'created', 'user_id' : current_user.id, 'attrs' : job_attrs }
    for name, value in form.data.items():
        if name == 'name':
            data['name'] = value
        elif name == 'sequence_identifier':
            job_attrs[name] = str(value)[1:]
        elif name != 'csrf_token' and name != 'file' and name != 'submit':
            job_attrs[name] = str(value)

    if extra_file is not None:
        job_attrs['extra_file'] = 'extra_file'
    job = Job(**data)
    job.save()

    # If there is no job name, then set the job id as the job name.
    if job.name == '':
        job.name = str(job.id)
        job.save()

    client = arc.Client('newriver1.arc.vt.edu', arc.ARC_USER)
    remote_path = arc.get_remote_path(arc.ARC_USER, job.id)
    client.run('mkdir {}'.format(remote_path))

    # The path where all output files are written to is the project's directory.
    # NOTE: not all simulators have an input file (ex. xs)
    if hasattr(form, 'file'):
        project_dir = os.path.join(arc.ARC_DIR, str(job.id))
        filename = form.file.data.filename
        tmp_path = os.path.join('/tmp', filename)
        form.file.data.save(tmp_path)

        client.put_file(tmp_path, os.path.join(remote_path, 'input.fasta'))

    if extra_file is not None:
        tmp_path = os.path.join('/tmp', 'extra_file')
        extra_file.data.save(tmp_path)
        client.put_file(tmp_path, os.path.join(remote_path, 'extra_file'))

    client.close()
    start_job.apply_async(args=[str(job.id)])


def submit_retry(job):
    # delay for a day (in seconds)
    delay = 60 * 60 * 24
    start_job.apply_async(args=[str(job.id)], countdown=delay)