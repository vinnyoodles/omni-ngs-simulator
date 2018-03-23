from bear import PARAMETRIC_ABUNDANCE

SIMULATORS = {
    'bear.parametric_abundance': PARAMETRIC_ABUNDANCE
}

def sim_json():
    """
        Converts the SIMULATORS dictionary into a nested dictionary where
        the '.' denotes a nested level. This is due to multiple simulators
        sharing the same root name so it requires a subname (nested level).
    """
    result = {}
    for key in SIMULATORS:
        name, subname = key.split('.')
        if name not in result:
            result[name] = {}

        result[name][subname] = SIMULATORS[key]
    return result

def parse_commandline(sim, params):
    """
        Creates the command line input for running a job. Because subprocess.Popen requires an array
        of arguments, the output will be in an array format.

        NOTE: this assumes the params input contains all necessary values

        = Parameters =
        sim          : dict   = specific simulator dictionary 
        params       : dict   = dictionary of arguments to pass to the job when run

        = Return =
        array                 = arguments for subprocess.Popen
    """
    arguments = sim['format'].format(**params).split()
    return [sim['command']] + arguments
