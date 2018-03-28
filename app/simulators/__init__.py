# TODO: make sure fragsim is available in the PATH.
SIMULATORS = {
    'bear.parametric_abundance': {
        'command': 'parametric_abundance.pl',
        'arguments': ['input', 'complexity'],
        'defaults': {
            'complexity': 'high'
        },
        'format': '{input} {complexity}',
        'stdout': True,
        'title': 'Bear - Parametric Abundance',
        'caption': 'Generate abundance values derived from power functions that can correspond to metagenomic communities with low, medium, or high species complexity.',
        'route': 'bear_parametric_abundance'
    },

    '454sim': {
        'command': 'fragsim',
        'arguments': ['frag_count', 'frag_length', 'flow_simulation_count', 'generation', 'output'],
        'defaults': {
            'frag_count': 1000000,
            'frag_length': 1000,
            'flow_simulation_count': 800,
            'generation': 'Ti'
        },
        'format': '-c {frag_count} -l {frag_length} | 454sim -n {flow_simulation_count}-o {output}',
        'stdout': True,
        'title': '454Sim',
        'caption': 'Process standard FASTA and generate reads, one for each FASTA entry present in the file starting from the first base and until either the sequence ends or the simulated read ends.',
        'route': 'sim454'
    }
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
