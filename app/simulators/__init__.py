# TODO: make sure fragsim is available in the PATH.
SIMULATORS = {
    'bear.parametric_abundance': {
        'command': 'parametric_abundance.pl',
        'arguments': ['input', 'complexity'],
        'defaults': {
            'complexity': 'high'
        },
        'format': '{input} {complexity}',
        'optional': [],
        'stdout': True,
        'title': 'Bear - Parametric Abundance',
        'caption': 'Generate abundance values derived from power functions that can correspond to metagenomic communities with low, medium, or high species complexity.',
        'route': 'bear_parametric_abundance'
    },

    '454sim': {
        'command': 'fragsim',
        'arguments': ['input', 'frag_count', 'frag_length', 'flow_simulation_count', 'generation', 'output'],
        'defaults': {
            'frag_count': 1000000,
            'frag_length': 1000,
            'flow_simulation_count': 800,
            'generation': 'Ti'
        },
        'optional': [],
        'format': '-c {frag_count} -l {frag_length} {input} | 454sim -n {flow_simulation_count} -o {output}',
        'stdout': False,
        'title': '454Sim',
        'caption': 'Process standard FASTA and generate reads, one for each FASTA entry present in the file starting from the first base and until either the sequence ends or the simulated read ends.',
        'route': 'sim_454'
    },

    'art.solid': {
        'command': 'art_SOLiD',
        'arguments': ['input', 'output', 'read_len', 'fold_coverage'],
        'defaults': {},
        'format': '{input} {output} {read_len} {fold_coverage}',
        'optional': [],
        'stdout': False,
        'title': 'ART - SOLiD',
        'caption': 'ART generates sequence read data according to the empirical read quality profile summarized from large real read data. ART has been used for benchmarking methods and tools for next-generation sequencing data analysis, including read alignment, de novo assembly, detection of SNP, CNV, or other structure variation.',
        'route': 'art_solid'
    },
    'art.illumina': {
        'command': 'art_illumina',
        'arguments': ['input', 'output', 'sequencing_system', 'read_length', 'fold_coverage', 'num_reads_per_sequence', 'mean_fragsize', 'std_fragsize'],
        'defaults': {},
        'format': '-ss {sequencing_system} -sam -i {input} -l {read_length} -o {output}',
        'optional': [],
        'stdout': False,
        'title': 'ART - Illumina',
        'caption': 'ART generates sequence read data according to the empirical read quality profile summarized from large real read data. ART has been used for benchmarking methods and tools for next-generation sequencing data analysis, including read alignment, de novo assembly, detection of SNP, CNV, or other structure variation.',
        'route': 'art_illumina'
    },
    'art.454': {
        'command': 'art_454',
        'arguments': ['input', 'output', 'fold_coverage', 'mean_frag_len', 'std_dev', 'random_seed'],
        'defaults': {},
        'optional': ['mean_frag_len, std_dev', 'random_seed'],
        'format': '{random_seed} {input} {output} {fold_coverage} {mean_frag_len} {std_dev}',
        'stdout': False,
        'title': 'ART - 454',
        'caption': 'ART generates sequence read data according to the empirical read quality profile summarized from large real read data. ART has been used for benchmarking methods and tools for next-generation sequencing data analysis, including read alignment, de novo assembly, detection of SNP, CNV, or other structure variation.',
        'route': 'art_454'
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
