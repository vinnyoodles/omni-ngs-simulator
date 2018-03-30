import subprocess, os
from . import celery
from simulators import SIMULATORS, parse_commandline
from flask_login import current_user
from app.models import Job

@celery.task
def start_job(job_id, sim_id, params, output_file):
    """
        This is the main function to be consumed by the celery instance.
        This must be well defined and flexible enough to handle a variety of
        jobs and parameters.

        All simulator objects must be a dictionary of key/value pairs and
        must follow the format:

        {
            command: Executable name to be run in the command line.

            arguments: Array of required argument names that will be formatted in a given manner.

            defaults: Dictionary where the keys represent the argument name and the value is the default value of the argument.
               If no arguments have a default value, then this should be an empty dictionary.

            format: String denoting the format of arguments.
                String formatting docs: https://docs.python.org/2/library/string.html#custom-string-formatting

            stdout: Boolean denoting whether the output is sent to stdout or directly to a file.
                True if command sends to stdout (writing to output file will have to be done manually)
                False otherwise

            title:  String that will be rendered in application.

            caption:  String that will be rendered in application.

            route:  String representing the function of the specific simulator flask route.
        }

        The function should handle any updates to the database.

        = Parameters =
        sim_id       : string   = valid string that denotes the job (job is valid if found in SIMULATORS dict)
        params       : dict     = dictionary of arguments to pass to the job when run

        = Return =
        boolean = the status of the job (true=success, false=failed)
            The cause of failuer will will be written to the mongo database
    """

    job = Job.objects(id=job_id).first()
    job.status = 'started'
    job.save()

    # Check if job is valid and well defined.
    if sim_id is None or sim_id not in SIMULATORS:
        job.status = 'failed'
        job.err = 'Invalid sim id'
        job.save()
        return False

    # The output is always written to a file, if no filename is passed, then this is an invalid job.
    if output_file is None:
        job.status = 'failed'
        job.err = 'Missing output file'
        job.save()
        return False

    sim = SIMULATORS[sim_id]

    # Validate parameters.
    for arg in sim['arguments']:
        if arg not in params:
            # If the missing parameter exists in the default dictionary, then use that and continue.
            if arg in sim['defaults']:
                params[arg] = sim['defaults'][arg]
                continue

            elif arg in sim['optional']:
                continue

            job.status = 'failed'
            job.err = 'Missing argument: {}'.format(arg)
            job.save()
            return False

    commandline = parse_commandline(sim, params)

    try:
        if sim['stdout']:
            output_file = open(output_file, 'w+')
            process = subprocess.Popen(commandline, stdout=output_file)
        else:
            process = subprocess.Popen(commandline)
    except IOError as err:
        job.status = 'failed'
        job.err = 'IOError: {}'.format(str(err))
        job.save()
        return False

    process.wait()

    job.status = 'completed'
    job.save()
    return job_id

def create_and_start_job(sim_id, name, command_args, file):
    data = {
        'status'    : 'pending',
        'simulator' : sim_id,
        'user_id'   : current_user.id,
        'name'      : name
    }
    job = Job(**data)

    # If there is no job name, then set the job id as the job name.
    if name is None:
        job.name = name = str(job.id)

    job.save()

    # The path where all output files are written to is the project's directory.
    # TODO: for dev purposes, this is okay (change for production)
    prefix = '{}_{}'.format(sim_id, job.id).replace('.', '_')
    input_filename = os.path.join('/app', '{}.in'.format(prefix))
    output_filename = os.path.join('/app', '{}.out'.format(prefix))
    file.save(input_filename)

    command_args['input'] = input_filename
    command_args['output'] = output_filename

    # Omit the input filename for db storage
    arg_clone = command_args.copy()
    arg_clone['input'] = '<input>'
    arg_clone['output'] = '<output>'

    job.command = ' '.join(parse_commandline(SIMULATORS[sim_id], arg_clone))
    job.save()
    start_job.apply_async(args=[str(job.id), sim_id, command_args, output_filename])
