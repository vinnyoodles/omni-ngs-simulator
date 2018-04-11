SIMULATORS = {
    '454sim': {
        'title': '454Sim',
        'caption': 'Process standard FASTA and generate reads, one for each FASTA entry present in the file starting from the first base and until either the sequence ends or the simulated read ends.',
        'route': 'sim_454',
        'arguments': [ 'input', 'output', 'frag_count', 'frag_length', 'flow_simulation_count', 'generation' ],
        'ready': True
    },

    'artificialfastqgenerator': {
        'title': 'ArtificialFastqGenerator',
        'caption': 'Outputs artificial FASTQ files that are derived from the reference. The user can customise DNA template/read length, gap size between paired-end reads, target coverage, whether to use quality scores taken from existing FASTQ files, and whether to simulate sequencing errors. Detailed coverage and error summary statistics are outputted.',
        'route': 'artificial_fastq_generator',
        'arguments': [ 'input', 'output', 'sequence_identifier', 'coverage_mean', 'peak_coverage_mean', 'gc_content_peak', 'coverage_std_dev', 'read_length', 'mean_length', 'std_dev' ],
        'ready': True
    },

    'art_solid': {
        'title': 'ART - SOLiD',
        'caption': 'ART generates sequence read data according to the empirical read quality profile summarized from large real read data. ART has been used for benchmarking methods and tools for next-generation sequencing data analysis, including read alignment, de novo assembly, detection of SNP, CNV, or other structure variation.',
        'route': 'art_solid',
        'arguments': [ 'input', 'output', 'read_len','simulation_type','random_seed','fold_coverage','mean_frag_len','std_dev' ],
        'ready': True
    },

    'art_454': {
        'title': 'ART - 454',
        'caption': 'ART generates sequence read data according to the empirical read quality profile summarized from large real read data. ART has been used for benchmarking methods and tools for next-generation sequencing data analysis, including read alignment, de novo assembly, detection of SNP, CNV, or other structure variation.',
        'route': 'art_454',
        'arguments': [ 'input', 'output', 'random_seed', 'simulation_type', 'fold_coverage', 'mean_frag_len', 'std_dev' ],
        'ready': True
    },

    'curesim': {
        'title': 'CuReSim',
        'caption': 'Customized read simulator generates synthetic NGS reads, supporting read simulation for major letter-base sequencing platforms.',
        'route': 'curesim',
        'arguments': [ 'input', 'output', 'read_count', 'read_mean', 'read_size_std_dev', 'random_read_count', 'deletion_rate', 'insertion_rate', 'substitution_rate' ],
        'ready': True
    }, 

    'dwgsim': {
        'title': 'DWGSIM',
        'caption': 'Whole Genome Simulator for Next-Generation Sequencing, based off of wgsim but handles ABI SOLiD and Ion Torrent data, as well as various assumptions about aligners and positions of indels.',
        'route': 'dwgsim',
        'arguments': [ 'input', 'output', 'pair_outer_distance', 'distance_std_dev', 'mean_coverage', 'mutation_rate', 'mutation_frequency', 'mutation_indel_percentage', 'indel_extension_rate', 'min_indel_length', 'random_read_probability', 'technology', 'random_seed' ],
        'ready': True
    },

    'mason_sanger': {
        'title': 'Mason - Sanger',
        'caption': 'Simulate NGS reads given a genome with variants for a given donor to use as the source.',
        'route': 'mason_sanger',
        'arguments': [ 'input', 'output', 'random_seed', 'read_count', 'random_source_sequence_length', 'a_probability', 'c_probability', 'g_probability', 'mismatch_begin_probability', 'mismatch_end_probability', 'insertion_begin_probability', 'insertion_end_probability', 'deletion_begin_probability', 'deletion_end_probability' ],
        'ready': True
    },

    'mason_illumina': {
        'title': 'Mason - Illumina',
        'caption': 'Simulate NGS reads given a genome with variants for a given donor to use as the source.',
        'route': 'mason_illumina',
        'arguments': [ 'input', 'output', 'random_seed', 'read_count', 'random_source_sequence_length', 'a_probability', 'c_probability', 'g_probability', 'insertion_probability', 'deletion_probability', 'avg_mismatch_probability', 'first_base_mismatch_probability', 'last_base_mismatch_probability' ],
        'ready': True
    },

    'pbsim': {
        'title': 'Pbsim',
        'caption': 'PacBio reads simulater (called PBSIM) in which sampling-based and model-based simulations are implemented.',
        'route': 'pbsim',
        'arguments': [ 'input', 'output', 'min_length', 'max_length', 'min_accuracy', 'max_accuracy', 'substition_percentage', 'insertion_percentage', 'deletion_percentage', 'random_seed', 'extra_file' ],
        'ready': True
    },
    'pirs': {
        'title': 'pIRS',
        'caption': 'A tool for simulating paired-end reads from a reference genome. It is optimized for simulating reads similar to those generated from the Illumina platform.',
        'route': 'pirs',
        'arguments': [ 'input', 'output', 'read_len', 'coverage', 'insertion_len', 'std_dev_insertion_len', 'random_seed' ],
        'ready': True
    },

    'wgsim': {
        'title': 'wgsim',
        'caption': 'simulating sequence reads from a reference genome. It is able to simulate diploid genomes with SNPs and insertion/deletion (INDEL) polymorphisms, and simulate reads with uniform substitution sequencing errors.',
        'route': 'wgsim',
        'arguments': [ 'input', 'output', 'base_error_rate', 'outer_distance', 'std_dev', 'read_pair_count', 'first_read_len', 'second_read_len', 'mutation_rate', 'indel_fraction', 'indel_extension_rate', 'random_seed' ],
        'ready': True
    },

    'xs': {
        'title': 'XS',
        'caption': 'A FASTQ read simulation tool, flexible, portable (does not need a reference sequence) and aimed at testing computing infrastructures, namely cloud computing of large-scale projects, and testing FASTQ compression algorithms. Moreover, XS offers the possibility of simulating the three main FASTQ components individually (headers, DNA sequences and quality-scores).',
        'route': 'xs',
        'arguments': [ 'output', 'technology', 'header_format', 'read_per_file', 'a_probability', 'c_probability', 'g_probability', 't_probability', 'n_probability', 'repeat_count', 'repeat_min', 'repeat_max', 'mutation_frequency', 'random_seed' ],
        'ready': True
    },

    'eagle': {
        'title' : 'EAGLE',
        'caption': 'Enhanced Artificial Genome Engine, next generation sequencing reads simulator, is designed to simulate the behaviour of Illumina\'s Next Generation Sequencing instruments, in order to facilitate the development and testing of downstream applications.',
        'route': 'eagle',
        'ready': False
    },

    'fastqsim': {
        'title': 'FASTQSim',
        'caption': 'FASTQSim: Platform-Independent Data Characterizationa and In Silico Read Generation for NGS Datasets',
        'route': 'fastqsim',
        'ready': False
    },

    'flowsim': {
        'title': 'Flowsim',
        'caption': 'Generates simulated reads from them mimicing Roche\'s 454 pyrosequencing technology, writing output in 454\'s native SFF format. The flowgram generation is based on empirical distributions derived from real data',
        'route': 'flowsim',
        'ready': False
    }, 

    'gemsim': {
        'title': 'GemSim',
        'caption': 'A NGS simulator capable of generating single or paired-end reads for any sequencing technology compatible with the generic formats SAM and FASTQ. GemSIM creates and uses empirically derived, sequence-context based error models to realistically emulate individual sequencing runs and/or technologies.',
        'route': 'gemsim',
        'ready': False
    },

    'grinder': {
        'title': 'Grinder',
        'caption': 'A bioinformatics tool to create simulated omic shotgun and amplicon sequence libraries for all main sequencing platforms.',
        'route':'grinder',
        'arguments': [ 'input', 'output', 'total_reads', 'read_dist', 'insert_dist', 'mate_orientation', 'direction', 'length_bias', 'copy_bias', 'random_seed', 'desc_track' ],
        'ready': True
    },

    'metasim': {
        'title': 'MetaSim',
        'caption': 'Generates synthetic reads that reflect the diverse taxonomical composition of typical metagenome data sets, allows the user to design a metagenome by specifying the number of genomes present at different levels of the NCBI taxonomy, and then to collect reads from the metagenome using a simulation of a number of different sequencing technologies.',
        'route': 'metasim',
        'ready': False
    },

    'nessm': {
        'title': 'NeSSM',
        'caption': 'Next-generation Sequencing Simulator for Metagenomics, combining complete genomes currently available, a community composition table, and sequencing parameters, it can simulate metagenome sequencing better than existing systems.',
        'route': 'nessm',
        'ready': False
    },

    'readsim': {
        'title': 'ReadSim',
        'caption': 'ReadSim is a fast and simple reads simulator to target long reads such as PacBio or Nanopore.',
        'route': 'readsim',
        'ready': False
    },

    'sinc': {
        'title': 'SInC',
        'caption': 'An accurate and fast error-model based simulator for SNPs, Indels and CNVs coupled with a read generator for short-read sequence data.',
        'route': 'sinc',
        'ready': False
    },

    'simseq': {
        'title': 'SimSeq',
        'caption': 'An illumina paired-end and mate-pair short read simulator, attempts to model as many of the quirks that exist in Illumina data as possible. Some of these quirks include the potential for chimeric reads, and non-biotinylated fragment pull down in mate-pair libraries.',
        'route': 'simseq',
        'ready': False
    },

    'simhtsd': {
        'title': 'simhtsd',
        'caption': 'Given a reference sequence, simhtsd will create a large set of short nucleotide reads, simulating the output from today\'s high-throughput DNA sequencers, such as the Illumina Genome Analyzer II.',
        'route': 'simhtsd',
        'ready': False
    },

    'simngs': {
        'title': 'simNGS',
        'caption': 'Simulating observations from Illumina sequencing machines using the statistical models behind the AYB base-calling software.',
        'route': 'simngs',
        'ready': False
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
        name, subname = key.split('_')
        if name not in result:
            result[name] = {}

        result[name][subname] = SIMULATORS[key]
    return result