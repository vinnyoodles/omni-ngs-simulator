import subprocess, os
from . import celery
from simulators import SIMULATORS
from flask_login import current_user
from app.models import Job
import arc

ARC_DIR = '$WORK/omningssimulator'
ARC_USER = 'vincentl'
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
        return False

    job.status = 'queued'
    job.save()

    # Validate simulator
    sim_id = job.simulator
    if sim_id is None or sim_id not in SIMULATORS:
        job.status = 'failed'
        job.err = 'Invalid simulator or simulator does not exist'
        job.save()
        return False

    sim = SIMULATORS[sim_id]

    # Validate parameters.
    for arg in sim['arguments']:
        if arg == 'input' or arg == 'output':
            continue
        if arg not in job.attrs:
            job.status = 'failed'
            job.err = 'Missing argument: {}'.format(arg)
            job.save()
            return False

    remote_path = arc.get_remote_path(ARC_USER, job.id)
    input_path = os.path.join(remote_path, 'input.fasta')
    output_path = os.path.join(remote_path, 'output')

    client = arc.Client('newriver1.arc.vt.edu', ARC_USER)
    try:
        current_job_count = int(client.run('qstat | grep {} | wc -l'.format(ARC_USER)))
        if current_job_count > JOB_THRESHOLD:
            submit_retry(job)
    except ValueError:
        submit_retry(job)
        return False

    # TODO: submit job to arc
    print(job.attrs)
    # client.run()
    client.close()

    job.status = 'completed'
    job.save()
    return True

def create_and_start_job(sim_id, form):
    job_attrs = dict()
    data = { 'simulator' : sim_id, 'status' : 'created', 'user_id' : current_user.id, 'attrs' : job_attrs }
    for name, value in form.data.items():
        if name == 'name':
            data['name'] = value
        elif name != 'csrf_token' and name != 'file' and name != 'submit':
            job_attrs[name] = str(value)
    job = Job(**data)
    job.save()

    # # If there is no job name, then set the job id as the job name.
    if job.name == '':
        job.name = str(job.id)
        job.save()

    # # The path where all output files are written to is the project's directory.
    project_dir = os.path.join(ARC_DIR, str(job.id))
    filename = form.file.data.filename
    tmp_path = os.path.join('/tmp', filename)
    form.file.data.save(tmp_path)

    remote_path = arc.get_remote_path(ARC_USER, job.id)
    client = arc.Client('newriver1.arc.vt.edu', ARC_USER)
    client.run('mkdir {}'.format(remote_path))
    client.put_file(tmp_path, os.path.join(remote_path, 'input.fasta'))
    client.close()

    start_job.apply_async(args=[str(job.id)])


def submit_retry(job):
    # delay for a day (in seconds)
    delay = 60 * 60 * 24
    start_job.apply_async(args=[str(job.id)], countdown=delay)