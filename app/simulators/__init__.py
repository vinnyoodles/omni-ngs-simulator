SIMULATORS = {
    '454sim': {
        'title': '454Sim',
        'caption': 'Process standard FASTA and generate reads, one for each FASTA entry present in the file starting from the first base and until either the sequence ends or the simulated read ends.',
        'route': 'sim_454',
        'ready': True
    },

    'artificialfastqgenerator': {
        'title': 'ArtificialFastqGenerator',
        'caption': 'Outputs artificial FASTQ files that are derived from the reference. The user can customise DNA template/read length, gap size between paired-end reads, target coverage, whether to use quality scores taken from existing FASTQ files, and whether to simulate sequencing errors. Detailed coverage and error summary statistics are outputted.',
        'route': 'artificial_fastq_generator',
        'ready': True
    },

    'art.solid': {
        'title': 'ART - SOLiD',
        'caption': 'ART generates sequence read data according to the empirical read quality profile summarized from large real read data. ART has been used for benchmarking methods and tools for next-generation sequencing data analysis, including read alignment, de novo assembly, detection of SNP, CNV, or other structure variation.',
        'route': 'art_solid',
        'ready': True
    },

    'art.454': {
        'title': 'ART - 454',
        'caption': 'ART generates sequence read data according to the empirical read quality profile summarized from large real read data. ART has been used for benchmarking methods and tools for next-generation sequencing data analysis, including read alignment, de novo assembly, detection of SNP, CNV, or other structure variation.',
        'route': 'art_454',
        'ready': True
    },

    'curesim': {
        'title': 'CuReSim',
        'caption': 'Customized read simulator generates synthetic NGS reads, supporting read simulation for major letter-base sequencing platforms.',
        'route': 'curesim',
        'ready': True
    }, 

    'dwgsim': {
        'title': 'DWGSIM',
        'caption': 'Whole Genome Simulator for Next-Generation Sequencing, based off of wgsim but handles ABI SOLiD and Ion Torrent data, as well as various assumptions about aligners and positions of indels.',
        'route': 'dwgsim',
        'ready': True
    },

    'mason.sanger': {
        'title': 'Mason - Sanger',
        'caption': 'Simulate NGS reads given a genome with variants for a given donor to use as the source.',
        'route': 'mason_sanger',
        'ready': True
    },

    'mason.illumina': {
        'title': 'Mason - Illumina',
        'caption': 'Simulate NGS reads given a genome with variants for a given donor to use as the source.',
        'route': 'mason_illumina',
        'ready': True
    },

    'pbsim': {
        'title': 'Pbsim',
        'caption': 'PacBio reads simulater (called PBSIM) in which sampling-based and model-based simulations are implemented.',
        'route': 'pbsim',
        'ready': True
    },
    'pirs': {
        'title': 'pIRS',
        'caption': 'A tool for simulating paired-end reads from a reference genome. It is optimized for simulating reads similar to those generated from the Illumina platform.',
        'route': 'pirs',
        'ready': True
    },

    'wgsim': {
        'title': 'wgsim',
        'caption': 'simulating sequence reads from a reference genome. It is able to simulate diploid genomes with SNPs and insertion/deletion (INDEL) polymorphisms, and simulate reads with uniform substitution sequencing errors.',
        'route': 'wgsim',
        'ready': True
    },

    'xs': {
        'title': 'XS',
        'caption': 'A FASTQ read simulation tool, flexible, portable (does not need a reference sequence) and aimed at testing computing infrastructures, namely cloud computing of large-scale projects, and testing FASTQ compression algorithms. Moreover, XS offers the possibility of simulating the three main FASTQ components individually (headers, DNA sequences and quality-scores).',
        'route': 'xs',
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
        'ready': False
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
