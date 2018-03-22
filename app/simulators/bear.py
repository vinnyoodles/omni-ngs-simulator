PARAMETRIC_ABUNDANCE = {
    'command': 'parametric_abundance.pl',
    'arguments': ['multi_fasta', 'complexity'],
    'format': '{multi_fasta} {complexity}',
    'stdout': True

    'title': 'BEAR - Parametric Abundance',
    'caption': 'Generate abundance values derived from power functions that can correspond to metagenomic communities with low, medium, or high species complexity.',
    'route': 'simulators.bear_parametric_abundance'
}