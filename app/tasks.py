import subprocess, os
from app import celery
from simulators import SIMULATORS, parse_commandline

# The path where all output files are written to.
# TODO: for dev purposes, it is the current directory (update for production)
OUTPUT_DIR = '/app'

@celery.task
def start_job(job_name, params, output_file):
    """
        This is the main function to be consumed by the celery instance.
        This must be well defined and flexible enough to handle a variety of
        jobs and parameters.

        All simulator objects must be a dictionary of key/value pairs and
        must follow the format:

        {
            command: Executable name to be run in the command line.

            arguments: Array of required argument names that will be formatted in a given manner.

            format: String denoting the format of arguments.
                String formatting docs: https://docs.python.org/2/library/string.html#custom-string-formatting

            stdout: Boolean denoting whether the output is sent to stdout or directly to a file.
                True if command sends to stdout (writing to output file will have to be done manually)
                False otherwise
        }

        The function should handle any updates to the database.

        = Parameters =
        job_name     : string   = valid string that denotes the job (job is valid if found in SIMULATORS dict)
        params       : dict     = dictionary of arguments to pass to the job when run

        = Return =
        boolean = the status of the job (true=success, false=failed)
            The cause of failuer will will be written to the mongo database
    """

    # Check if job is valid and well defined.
    # job_name, params, output_file = ['bear.parametric_abundance', { 'output' : 'foo' }, 'i_hope_this_works.out']
    if job_name is None or job_name not in SIMULATORS:
        # TODO: update database failure (invalid job name)
        return job_name

    # The output is always written to a file, if no filename is passed, then this is an invalid job.
    if output_file is None:
        # TODO: update database failure (missing output file)
        return output_file

    job = SIMULATORS[job_name]

    # Validate parameters.
    for arg in job['arguments']:
        if arg not in params:
            # TODO: update database failure (invalid job arguments)
            return arg

    commandline = parse_commandline(job, params)

    try:
        if job['stdout']:
            output_file = open(os.path.join(OUTPUT_DIR, output_file), 'w+')
            process = subprocess.Popen(commandline, stdout=output_file)
        else:
            process = subprocess.Popen(commandline)
    except IOError as err:
        # TODO: update database failure (i/o error)
        return str(err)

    process.wait()

    # TODO: update database success
    return True