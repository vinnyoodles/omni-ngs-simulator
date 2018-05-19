SIMULATORS = {
    '454sim': { 
        'title': '454Sim',
        'caption': 'Process standard FASTA and generate reads, one for each FASTA entry present in the file starting from the first base and until either the sequence ends or the simulated read ends.',
        'route': 'sim_454',
        'arguments': [ 'input', 'output', 'frag_count', 'frag_length', 'flow_simulation_count', 'generation' ],
        'ref_db': True,
        'genomics': True,
        'tech': ['454'],
        'variants': True,
        'ready': True
    },

    'artificialfastqgenerator': {
        'title': 'ArtificialFastqGenerator',
        'caption': 'Outputs artificial FASTQ files that are derived from the reference. The user can customise DNA template/read length, gap size between paired-end reads, target coverage, whether to use quality scores taken from existing FASTQ files, and whether to simulate sequencing errors. Detailed coverage and error summary statistics are outputted.',
        'route': 'artificial_fastq_generator',
        'arguments': [ 'input', 'output', 'sequence_identifier', 'coverage_mean', 'peak_coverage_mean', 'gc_content_peak', 'coverage_std_dev', 'read_length', 'mean_length', 'std_dev' ],
        'ref_db': True,
        'genomics': True,
        'tech': ['illumina'],
        'variants': True,
        'ready': True
    },

    'art_solid': {
        'title': 'ART - SOLiD',
        'caption': 'ART generates sequence read data according to the empirical read quality profile summarized from large real read data. ART has been used for benchmarking methods and tools for next-generation sequencing data analysis, including read alignment, de novo assembly, detection of SNP, CNV, or other structure variation.',
        'route': 'art_solid',
        'arguments': [ 'input', 'output', 'read_len','simulation_type','random_seed','fold_coverage','mean_frag_len','std_dev' ],
        'ref_db': True,
        'genomics': True,
        'tech': ['solid'],
        'variants': True,
        'ready': True
    },

    'art_454': {
        'title': 'ART - 454',
        'caption': 'ART generates sequence read data according to the empirical read quality profile summarized from large real read data. ART has been used for benchmarking methods and tools for next-generation sequencing data analysis, including read alignment, de novo assembly, detection of SNP, CNV, or other structure variation.',
        'route': 'art_454',
        'arguments': [ 'input', 'output', 'random_seed', 'simulation_type', 'fold_coverage', 'mean_frag_len', 'std_dev' ],
        'ref_db': True,
        'genomics': True,
        'tech': ['454'],
        'variants': True,
        'ready': True
    },

    'art_illumina': {
        'title': 'ART - Illumina',
        'caption': 'ART generates sequence read data according to the empirical read quality profile summarized from large real read data. ART has been used for benchmarking methods and tools for next-generation sequencing data analysis, including read alignment, de novo assembly, detection of SNP, CNV, or other structure variation.',
        'route': 'art_illumina',
        'arguments': [ 'input', 'output', 'random_seed', 'simulation_type', 'fold_coverage', 'mean_frag_len', 'std_dev' ],
        'ref_db': True,
        'genomics': True,
        'tech': ['illumina'],
        'variants': True,
        'ready': False
    },

    'bear_genomics_454': {
        'title': 'BEAR - Genomics 454',
        'caption': 'BEAR is intended to be an easy-to-use collection of scripts for generating simulated WGS metagenomic reads with read lengths, quality scores, error profiles, and species abundances derived from real user-supplied WGS data.',
        'route': 'bear_genomics_454',
        'arguments': ['genomes_file','abundance_file','output_file','total_reads','longest_read','insert_mean_length','insert_stddev'],
        'ref_db': True,
        'genomics': True,
        'tech': ['454'],
        'variants': False,
        'ready': False
     },

    'bear_genomics_illumina': {
        'title': 'BEAR - Genomics Illumina',
        'caption': 'BEAR is intended to be an easy-to-use collection of scripts for generating simulated WGS metagenomic reads with read lengths, quality scores, error profiles, and species abundances derived from real user-supplied WGS data.',
        'route': 'bear_genomics_illumina',
        'arguments': ['genomes_file','abundance_file','output_file','total_reads','longest_read','insert_mean_length','insert_stddev'],
        'ref_db': True,
        'genomics': True,
        'tech': ['illumina'],
        'variants': False,
        'ready': False
     },

    'bear_genomics_iontorrent': {
        'title': 'BEAR - Genomics Iontorrent',
        'caption': 'BEAR is intended to be an easy-to-use collection of scripts for generating simulated WGS metagenomic reads with read lengths, quality scores, error profiles, and species abundances derived from real user-supplied WGS data.',
        'route': 'bear_genomics_iontorrent',
        'arguments': ['genomes_file','abundance_file','output_file','total_reads','longest_read','insert_mean_length','insert_stddev'],
        'ref_db': True,
        'genomics': True,
        'tech': ['iontorrent'],
        'variants': False,
        'ready': False
     },

    'bear_metagenomics_454': {
        'title': 'BEAR - Metagenomics 454',
        'caption': 'BEAR is intended to be an easy-to-use collection of scripts for generating simulated WGS metagenomic reads with read lengths, quality scores, error profiles, and species abundances derived from real user-supplied WGS data.',
        'route': 'bear_metagenomics_454',
        'arguments': ['metagenomics_file','abundance_file','output_file','total_reads','longest_read','insert_mean_length','insert_stddev'],
        'ref_db': True,
        'genomics': False,
        'tech': ['454'],
        'variants': False,
        'ready': False
     },

    'bear_metagenomics_illumina': {
        'title': 'BEAR - Metagenomics Illumina',
        'caption': 'BEAR is intended to be an easy-to-use collection of scripts for generating simulated WGS metagenomic reads with read lengths, quality scores, error profiles, and species abundances derived from real user-supplied WGS data.',
        'route': 'bear_metagenomics_illumina',
        'arguments': ['metagenomics_file','abundance_file','output_file','total_reads','longest_read','insert_mean_length','insert_stddev'],
        'ref_db': True,
        'genomics': False,
        'tech': ['illumina'],
        'variants': False,
        'ready': False
     },

    'bear_metagenomics_iontorrent': {
        'title': 'BEAR - Metagenomics Iontorrent',
        'caption': 'BEAR is intended to be an easy-to-use collection of scripts for generating simulated WGS metagenomic reads with read lengths, quality scores, error profiles, and species abundances derived from real user-supplied WGS data.',
        'route': 'bear_metagenomics_iontorrent',
        'arguments': ['metagenomics_file','abundance_file','output_file','total_reads','longest_read','insert_mean_length','insert_stddev'],
        'ref_db': True,
        'genomics': False,
        'tech': ['iontorrent'],
        'variants': False,
        'ready': False
     },    

    'curesim_illumina': { #
        'title': 'CuReSim - Illumina',
        'caption': 'Customized read simulator generates synthetic NGS reads, supporting read simulation for major letter-base sequencing platforms.',
        'route': 'curesim_illumina',
        'arguments': [ 'input', 'output', 'read_count', 'read_mean', 'read_size_std_dev', 'random_read_count', 'deletion_rate', 'insertion_rate', 'substitution_rate' ],
        'ref_db': True,
        'genomics': True,
        'tech': ['illumina'],
        'variants': True,
        'ready': True
    },

    'curesim_solid': { #
        'title': 'CuReSim - Solid',
        'caption': 'Customized read simulator generates synthetic NGS reads, supporting read simulation for major letter-base sequencing platforms.',
        'route': 'curesim_solid',
        'arguments': [ 'input', 'output', 'read_count', 'read_mean', 'read_size_std_dev', 'random_read_count', 'deletion_rate', 'insertion_rate', 'substitution_rate' ],
        'ref_db': True,
        'genomics': True,
        'tech': ['solid'],
        'variants': True,
        'ready': True
    }, 

    'curesim_iontorrent': { #
        'title': 'CuReSim - Iontorrent',
        'caption': 'Customized read simulator generates synthetic NGS reads, supporting read simulation for major letter-base sequencing platforms.',
        'route': 'curesim',
        'arguments': [ 'input', 'output', 'read_count', 'read_mean', 'read_size_std_dev', 'random_read_count', 'deletion_rate', 'insertion_rate', 'substitution_rate' ],
        'ref_db': True,
        'genomics': True,
        'tech': ['iontorrent'],
        'variants': True,
        'ready': True
    }, 

    'curesim_454': { #
        'title': 'CuReSim - 454',
        'caption': 'Customized read simulator generates synthetic NGS reads, supporting read simulation for major letter-base sequencing platforms.',
        'route': 'curesim_454',
        'arguments': [ 'input', 'output', 'read_count', 'read_mean', 'read_size_std_dev', 'random_read_count', 'deletion_rate', 'insertion_rate', 'substitution_rate' ],
        'ref_db': True,
        'genomics': True,
        'tech': ['454'],
        'variants': True,
        'ready': True
    },  

    'dwgsim_illumina': {#
        'title': 'DWGSIM - Illumina',
        'caption': 'Whole Genome Simulator for Next-Generation Sequencing, based off of wgsim but handles ABI SOLiD and Ion Torrent data, as well as various assumptions about aligners and positions of indels.',
        'route': 'dwgsim_illumina',
        'arguments': [ 'input', 'output', 'pair_outer_distance', 'distance_std_dev', 'mean_coverage', 'mutation_rate', 'mutation_frequency', 'mutation_indel_percentage', 'indel_extension_rate', 'min_indel_length', 'random_read_probability', 'technology', 'random_seed' ],
        'ref_db': True,
        'genomics': True,
        'tech': ['illumina'],
        'variants': False,
        'ready': True
    },

    'dwgsim_solid': {#
        'title': 'DWGSIM - Solid',
        'caption': 'Whole Genome Simulator for Next-Generation Sequencing, based off of wgsim but handles ABI SOLiD and Ion Torrent data, as well as various assumptions about aligners and positions of indels.',
        'route': 'dwgsim_solid',
        'arguments': [ 'input', 'output', 'pair_outer_distance', 'distance_std_dev', 'mean_coverage', 'mutation_rate', 'mutation_frequency', 'mutation_indel_percentage', 'indel_extension_rate', 'min_indel_length', 'random_read_probability', 'technology', 'random_seed' ],
        'ref_db': True,
        'genomics': True,
        'tech': ['solid'],
        'variants': False,
        'ready': True
    },

    'dwgsim_iontorrent': {#
        'title': 'DWGSIM - Iontorrent',
        'caption': 'Whole Genome Simulator for Next-Generation Sequencing, based off of wgsim but handles ABI SOLiD and Ion Torrent data, as well as various assumptions about aligners and positions of indels.',
        'route': 'dwgsim_iontorrent',
        'arguments': [ 'input', 'output', 'pair_outer_distance', 'distance_std_dev', 'mean_coverage', 'mutation_rate', 'mutation_frequency', 'mutation_indel_percentage', 'indel_extension_rate', 'min_indel_length', 'random_read_probability', 'technology', 'random_seed' ],
        'ref_db': True,
        'genomics': True,
        'tech': ['iontorrent'],
        'variants': False,
        'ready': True
    },

    'mason_genomics_454': {#
        'title': 'Mason - Genomics 454',
        'caption': 'Simulate NGS reads given a genome with variants for a given donor to use as the source.',
        'route': 'mason_genomics_454',
        'arguments': [ 'input', 'output', 'random_seed', 'read_count', 'random_source_sequence_length', 'a_probability', 'c_probability', 'g_probability', 'mismatch_begin_probability', 'mismatch_end_probability', 'insertion_begin_probability', 'insertion_end_probability', 'deletion_begin_probability', 'deletion_end_probability' ],
        'ref_db': True,
        'genomics': True,
        'tech': ['454'],
        'variants': False,
        'ready': True
    },

    'mason_genomics_sanger': {#
        'title': 'Mason - Genomics Sanger',
        'caption': 'Simulate NGS reads given a genome with variants for a given donor to use as the source.',
        'route': 'mason_genomics_sanger',
        'arguments': [ 'input', 'output', 'random_seed', 'read_count', 'random_source_sequence_length', 'a_probability', 'c_probability', 'g_probability', 'mismatch_begin_probability', 'mismatch_end_probability', 'insertion_begin_probability', 'insertion_end_probability', 'deletion_begin_probability', 'deletion_end_probability' ],
        'ref_db': True,
        'genomics': True,
        'tech': ['sanger'],
        'variants': False,
        'ready': True
    },

    'mason_genoimcs_illumina': {#
        'title': 'Mason - Genomics Illumina',
        'caption': 'Simulate NGS reads given a genome with variants for a given donor to use as the source.',
        'route': 'mason_genomics_illumina',
        'arguments': [ 'input', 'output', 'random_seed', 'read_count', 'random_source_sequence_length', 'a_probability', 'c_probability', 'g_probability', 'insertion_probability', 'deletion_probability', 'avg_mismatch_probability', 'first_base_mismatch_probability', 'last_base_mismatch_probability' ],
        'ref_db': True,
        'genomics': True,
        'tech': ['illumina'],
        'variants': False,
        'ready': True
    },

    'mason_metagenomics_illumina': {
        'title': 'Mason - Metagenomics Illumina',
        'caption': 'Simulate NGS reads given a genome with variants for a given donor to use as the source.',
        'route': 'mason_metagenomics_illumina',
        'arguments': [ 'input', 'output', 'random_seed', 'read_count', 'random_source_sequence_length', 'a_probability', 'c_probability', 'g_probability', 'insertion_probability', 'deletion_probability', 'avg_mismatch_probability', 'first_base_mismatch_probability', 'last_base_mismatch_probability' ],
        'ref_db': True,
        'genomics': False,
        'tech': ['illumina'],
        'variants': False,
        'ready': False
    },

    'mason_metagenomics_454': {
        'title': 'Mason - Metagenomics 454',
        'caption': 'Simulate NGS reads given a genome with variants for a given donor to use as the source.',
        'route': 'mason_metagenomics_454',
        'arguments': [ 'input', 'output', 'random_seed', 'read_count', 'random_source_sequence_length', 'a_probability', 'c_probability', 'g_probability', 'insertion_probability', 'deletion_probability', 'avg_mismatch_probability', 'first_base_mismatch_probability', 'last_base_mismatch_probability' ],
        'ref_db': True,
        'genomics': False,
        'tech': ['454'],
        'variants': False,
        'ready': False
    },


    'pbsim': {
        'title': 'Pbsim',
        'caption': 'PacBio reads simulater (called PBSIM) in which sampling-based and model-based simulations are implemented.',
        'route': 'pbsim',
        'arguments': [ 'input', 'output', 'min_length', 'max_length', 'min_accuracy', 'max_accuracy', 'substition_percentage', 'insertion_percentage', 'deletion_percentage', 'random_seed', 'extra_file' ],
        'tags': [ 'reference', 'genomics', 'variants', 'pacbio' ],
        'ref_db': True,
        'genomics': True,
        'tech': ['pacbio'],
        'variants': True,
        'ready': True
    },

    'pirs_genomics_illumina': {
        'title': 'pIRS - Genomics',
        'caption': 'A tool for simulating paired-end reads from a reference genome. It is optimized for simulating reads similar to those generated from the Illumina platform.',
        'route': 'pirs_genomics_illumina',
        'arguments': [ 'input', 'output', 'read_len', 'coverage', 'insertion_len', 'std_dev_insertion_len', 'random_seed' ],
        'ref_db': True,
        'genomics': True,
        'tech': ['illumina'],
        'variants': False,
        'ready': True
    },

    'pirs_metagenomics_illumina': {
        'title': 'pIRS - Metagenomics Illumina',
        'caption': 'A tool for simulating paired-end reads from a reference genome. It is optimized for simulating reads similar to those generated from the Illumina platform.',
        'route': 'pirs_metagenomics_illumina',
        'arguments': [ 'input', 'output', 'read_len', 'coverage', 'insertion_len', 'std_dev_insertion_len', 'random_seed' ],
        'ref_db': True,
        'genomics': False,
        'tech': ['illumina'],
        'variants': False,
        'ready': False
    },

    'wgsim_illumina': {
        'title': 'wgsim - Illumina',
        'caption': 'simulating sequence reads from a reference genome. It is able to simulate diploid genomes with SNPs and insertion/deletion (INDEL) polymorphisms, and simulate reads with uniform substitution sequencing errors.',
        'route': 'wgsim_illumina',
        'arguments': [ 'input', 'output', 'base_error_rate', 'outer_distance', 'std_dev', 'read_pair_count', 'first_read_len', 'second_read_len', 'mutation_rate', 'indel_fraction', 'indel_extension_rate', 'random_seed' ],
        'ref_db': True,
        'genomics': True,
        'tech': ['illumina'],
        'variants': False,
        'ready': True
    },

    'wgsim_solid': {
        'title': 'wgsim - Solid',
        'caption': 'simulating sequence reads from a reference genome. It is able to simulate diploid genomes with SNPs and insertion/deletion (INDEL) polymorphisms, and simulate reads with uniform substitution sequencing errors.',
        'route': 'wgsim_solid',
        'arguments': [ 'input', 'output', 'base_error_rate', 'outer_distance', 'std_dev', 'read_pair_count', 'first_read_len', 'second_read_len', 'mutation_rate', 'indel_fraction', 'indel_extension_rate', 'random_seed' ],
        'ref_db': True,
        'genomics': True,
        'tech': ['solid'],
        'variants': False,
        'ready': True
    },

    'xs_454': { #
        'title': 'XS - 454',
        'caption': 'A FASTQ read simulation tool, flexible, portable (does not need a reference sequence) and aimed at testing computing infrastructures, namely cloud computing of large-scale projects, and testing FASTQ compression algorithms. Moreover, XS offers the possibility of simulating the three main FASTQ components individually (headers, DNA sequences and quality-scores).',
        'route': 'xs_454',
        'arguments': [ 'output', 'technology', 'header_format', 'read_per_file', 'a_probability', 'c_probability', 'g_probability', 't_probability', 'n_probability', 'repeat_count', 'repeat_min', 'repeat_max', 'mutation_frequency', 'random_seed' ],
        'ref_db': False,
        'genomics': False,
        'tech': ['454'],
        'variants': False,
        'ready': True
    },

    'xs_iontorrent': {#
        'title': 'XS - Iontorrent',
        'caption': 'A FASTQ read simulation tool, flexible, portable (does not need a reference sequence) and aimed at testing computing infrastructures, namely cloud computing of large-scale projects, and testing FASTQ compression algorithms. Moreover, XS offers the possibility of simulating the three main FASTQ components individually (headers, DNA sequences and quality-scores).',
        'route': 'xs_iontorrent',
        'arguments': [ 'output', 'technology', 'header_format', 'read_per_file', 'a_probability', 'c_probability', 'g_probability', 't_probability', 'n_probability', 'repeat_count', 'repeat_min', 'repeat_max', 'mutation_frequency', 'random_seed' ],
        'ref_db': False,
        'genomics': False,
        'tech': ['iontorrent'],
        'variants': False,
        'ready': True
    },

    'xs_illumina': {#
        'title': 'XS - Illumina',
        'caption': 'A FASTQ read simulation tool, flexible, portable (does not need a reference sequence) and aimed at testing computing infrastructures, namely cloud computing of large-scale projects, and testing FASTQ compression algorithms. Moreover, XS offers the possibility of simulating the three main FASTQ components individually (headers, DNA sequences and quality-scores).',
        'route': 'xs_illumina',
        'arguments': [ 'output', 'technology', 'header_format', 'read_per_file', 'a_probability', 'c_probability', 'g_probability', 't_probability', 'n_probability', 'repeat_count', 'repeat_min', 'repeat_max', 'mutation_frequency', 'random_seed' ],
        'ref_db': False,
        'genomics': False,
        'tech': ['illumina'],
        'variants': False,
        'ready': True
    },

    'xs_solid': {#
        'title': 'XS - Solid',
        'caption': 'A FASTQ read simulation tool, flexible, portable (does not need a reference sequence) and aimed at testing computing infrastructures, namely cloud computing of large-scale projects, and testing FASTQ compression algorithms. Moreover, XS offers the possibility of simulating the three main FASTQ components individually (headers, DNA sequences and quality-scores).',
        'route': 'xs_solid',
        'arguments': [ 'output', 'technology', 'header_format', 'read_per_file', 'a_probability', 'c_probability', 'g_probability', 't_probability', 'n_probability', 'repeat_count', 'repeat_min', 'repeat_max', 'mutation_frequency', 'random_seed' ],
        'ref_db': False,
        'genomics': False,
        'tech': ['solid'],
        'variants': False,
        'ready': True
    },

    'eagle_454': {
        'title' : 'EAGLE - 454',
        'caption': 'Enhanced Artificial Genome Engine, next generation sequencing reads simulator, is designed to simulate the behaviour of Illumina\'s Next Generation Sequencing instruments, in order to facilitate the development and testing of downstream applications.',
        'route': 'eagle_454',
        'arguments':[''],
        'ref_db': True,
        'genomics': True,
        'tech': ['454'],
        'variants': False,
        'ready': False
    },

    'eagle_illumina': {
        'title' : 'EAGLE - Illumina',
        'caption': 'Enhanced Artificial Genome Engine, next generation sequencing reads simulator, is designed to simulate the behaviour of Illumina\'s Next Generation Sequencing instruments, in order to facilitate the development and testing of downstream applications.',
        'route': 'eagle_illumina',
        'arguments':[''],
        'ref_db': True,
        'genomics': True,
        'tech': ['illumina'],
        'variants': False,
        'ready': False
    },

    'eagle_pacbio': {
        'title' : 'EAGLE - PacBio',
        'caption': 'Enhanced Artificial Genome Engine, next generation sequencing reads simulator, is designed to simulate the behaviour of Illumina\'s Next Generation Sequencing instruments, in order to facilitate the development and testing of downstream applications.',
        'route': 'eagle',
        'arguments':[''],
        'ref_db': True,
        'genomics': True,
        'tech': ['pacbio'],
        'variants': False,
        'ready': False
    },

    'eagle_iontorrent': {
        'title' : 'EAGLE- Iontorrent',
        'caption': 'Enhanced Artificial Genome Engine, next generation sequencing reads simulator, is designed to simulate the behaviour of Illumina\'s Next Generation Sequencing instruments, in order to facilitate the development and testing of downstream applications.',
        'route': 'eagle_iontorrent',
        'arguments':[''],
        'ref_db': True,
        'genomics': True,
        'tech': ['iontorrent'],
        'variants': False,
        'ready': False
    },   

    'fastqsim_genomics_illumina': {
        'title': 'FASTQSim - Genomics Illumina',
        'caption': 'FASTQSim: Platform-Independent Data Characterizationa and In Silico Read Generation for NGS Datasets',
        'route': 'fastqsim_genomics_illumina',
        'arguments':[''],
        'ref_db': True,
        'genomics': True,
        'tech':['illumina'],
        'variants': False,
        'ready': False
    },

    'fastqsim_genomics_solid': {
        'title': 'FASTQSim - Genomics Solid',
        'caption': 'FASTQSim: Platform-Independent Data Characterizationa and In Silico Read Generation for NGS Datasets',
        'route': 'fastqsim_genomics_solid',
        'arguments':[''],
        'ref_db': True,
        'genomics': True,
        'tech':['solid'],
        'variants': False,
        'ready': False
    },

    'fastqsim_genomics_pacbio': {
        'title': 'FASTQSim - Genomics PacBio',
        'caption': 'FASTQSim: Platform-Independent Data Characterizationa and In Silico Read Generation for NGS Datasets',
        'route': 'fastqsim_genomics_pacbio',
        'arguments':[''],
        'ref_db': True,
        'genomics': True,
        'tech':['pacbio'],
        'variants': False,
        'ready': False
    },

    'fastqsim_genomics_iontorrent': {
        'title': 'FASTQSim - Genomics Iontorrent',
        'caption': 'FASTQSim: Platform-Independent Data Characterizationa and In Silico Read Generation for NGS Datasets',
        'route': 'fastqsim_genomics_iontorrent',
        'arguments':[''],
        'ref_db': True,
        'genomics': True,
        'tech':['iontorrent'],
        'variants': False,
        'ready': False
    },

    'fastqsim_metagenomics_illumina': {
        'title': 'FASTQSim - Metagenomics Illumina',
        'caption': 'FASTQSim: Platform-Independent Data Characterizationa and In Silico Read Generation for NGS Datasets',
        'route': 'fastqsim_metagenomics_illumina',
        'arguments':[''],
        'ref_db': True,
        'genomics': False,
        'tech':['illumina'],
        'variants': False,
        'ready': False
    },

    'fastqsim_metagenomics_solid': {
        'title': 'FASTQSim - Metagenomics Solid',
        'caption': 'FASTQSim: Platform-Independent Data Characterizationa and In Silico Read Generation for NGS Datasets',
        'route': 'fastqsim_metagenomics_solid',
        'arguments':[''],
        'ref_db': True,
        'genomics': False,
        'tech':['solid'],
        'variants': False,
        'ready': False
    },

    'fastqsim_metagenomics_pacbio': {
        'title': 'FASTQSim - Metagenomics PacBio',
        'caption': 'FASTQSim: Platform-Independent Data Characterizationa and In Silico Read Generation for NGS Datasets',
        'route': 'fastqsim_metagenomics_pacbio',
        'arguments':[''],
        'ref_db': True,
        'genomics': False,
        'tech':['pacbio'],
        'variants': False,
        'ready': False
    },

    'fastqsim_metagenomics_iontorrent': {
        'title': 'FASTQSim - Metagenomics Iontorrent',
        'caption': 'FASTQSim: Platform-Independent Data Characterizationa and In Silico Read Generation for NGS Datasets',
        'route': 'fastqsim_metagenomics_iontorrent',
        'arguments':[''],
        'ref_db': True,
        'genomics': False,
        'tech':['iontorrent'],
        'variants': False,
        'ready': False
    },

    'flowsim': {
        'title': 'Flowsim',
        'caption': 'Generates simulated reads from them mimicing Roche\'s 454 pyrosequencing technology, writing output in 454\'s native SFF format. The flowgram generation is based on empirical distributions derived from real data',
        'route': 'flowsim',
        'arguments':[''],
        'ref_db': True,
        'genomics': True,
        'tech':['454'],
        'variants': True,
        'ready': False
    }, 

    'gemsim_genomics_illumina': {
        'title': 'GemSim - Genomics Illumina',
        'caption': 'A NGS simulator capable of generating single or paired-end reads for any sequencing technology compatible with the generic formats SAM and FASTQ. GemSIM creates and uses empirically derived, sequence-context based error models to realistically emulate individual sequencing runs and/or technologies.',
        'route': 'gemsim_genomics_illumina',
        'arguments':[''],
        'ref_db': True,
        'genomics': True,
        'tech':['illumina'],
        'variants': False,
        'ready': False
    },

    'gemsim_genomics_454': {
        'title': 'GemSim - Genomics 454',
        'caption': 'A NGS simulator capable of generating single or paired-end reads for any sequencing technology compatible with the generic formats SAM and FASTQ. GemSIM creates and uses empirically derived, sequence-context based error models to realistically emulate individual sequencing runs and/or technologies.',
        'route': 'gemsim_genomics_454',
        'arguments':[''],
        'ref_db': True,
        'genomics': True,
        'tech':['454'],
        'variants': False,
        'ready': False
    },
    
    'gemsim_metagenomics_illumina': {
        'title': 'GemSim - Metagenomics Illumina',
        'caption': 'A NGS simulator capable of generating single or paired-end reads for any sequencing technology compatible with the generic formats SAM and FASTQ. GemSIM creates and uses empirically derived, sequence-context based error models to realistically emulate individual sequencing runs and/or technologies.',
        'route': 'gemsim_metagenomics',
        'arguments':[''],
        'ref_db': True,
        'genomics': False,
        'tech':['illumina'],
        'variants': False,
        'ready': False
    },

    'gemsim_metagenomics_454': {
        'title': 'GemSim - Metagenomics 454',
        'caption': 'A NGS simulator capable of generating single or paired-end reads for any sequencing technology compatible with the generic formats SAM and FASTQ. GemSIM creates and uses empirically derived, sequence-context based error models to realistically emulate individual sequencing runs and/or technologies.',
        'route': 'gemsim_metagenomics_454',
        'arguments':[''],
        'ref_db': True,
        'genomics': False,
        'tech':['454'],
        'variants': False,
        'ready': False
    },

    'grinder_genomics_illumina': {
        'title': 'Grinder - Genomics Illumina',
        'caption': 'A bioinformatics tool to create simulated omic shotgun and amplicon sequence libraries for all main sequencing platforms.',
        'route':'grinder_genomics_illumina',
        'arguments': [ 'input', 'output', 'total_reads', 'read_dist', 'insert_dist', 'mate_orientation', 'direction', 'length_bias', 'copy_bias', 'random_seed', 'desc_track' ],
        'ref_db': True,
        'genomics': True,
        'tech': ['illumina'],
        'variants': False,
        'ready': False
    },

    'grinder_genomics_454': {
        'title': 'Grinder - Genomics 454',
        'caption': 'A bioinformatics tool to create simulated omic shotgun and amplicon sequence libraries for all main sequencing platforms.',
        'route':'grinder_genomics_454',
        'arguments': [ 'input', 'output', 'total_reads', 'read_dist', 'insert_dist', 'mate_orientation', 'direction', 'length_bias', 'copy_bias', 'random_seed', 'desc_track' ],
        'ref_db': True,
        'genomics': True,
        'tech': ['454'],
        'variants': False,
        'ready': False
    },
    
    'grinder_genomics_sanger': {
        'title': 'Grinder - Genomics Sanger',
        'caption': 'A bioinformatics tool to create simulated omic shotgun and amplicon sequence libraries for all main sequencing platforms.',
        'route':'grinder_genomics_sanger',
        'arguments': [ 'input', 'output', 'total_reads', 'read_dist', 'insert_dist', 'mate_orientation', 'direction', 'length_bias', 'copy_bias', 'random_seed', 'desc_track' ],
        'ref_db': True,
        'genomics': True,
        'tech': ['sanger'],
        'variants': False,
        'ready': False
    },

    'grinder_metagenomics_illumina': {
        'title': 'Grinder - Metagenomics Illumina',
        'caption': 'A bioinformatics tool to create simulated omic shotgun and amplicon sequence libraries for all main sequencing platforms.',
        'route':'grinder_metagenomics_illumina',
        'arguments': [ 'input', 'output', 'total_reads', 'read_dist', 'insert_dist', 'mate_orientation', 'direction', 'length_bias', 'copy_bias', 'random_seed', 'desc_track' ],
        'ref_db': True,
        'genomics': False,
        'tech': ['illumina'],
        'variants': False,
        'ready': False
    },
    
    'grinder_metagenomics_454': {
        'title': 'Grinder - Metagenomics 454',
        'caption': 'A bioinformatics tool to create simulated omic shotgun and amplicon sequence libraries for all main sequencing platforms.',
        'route':'grinder_metagenomics_454',
        'arguments': [ 'input', 'output', 'total_reads', 'read_dist', 'insert_dist', 'mate_orientation', 'direction', 'length_bias', 'copy_bias', 'random_seed', 'desc_track' ],
        'ref_db': True,
        'genomics': False,
        'tech': ['454'],
        'variants': False,
        'ready': False
    },
    
    'grinder_metagenomics_sanger': {
        'title': 'Grinder - Metagenomics Sanger',
        'caption': 'A bioinformatics tool to create simulated omic shotgun and amplicon sequence libraries for all main sequencing platforms.',
        'route':'grinder_metagenomics_sanger',
        'arguments': [ 'input', 'output', 'total_reads', 'read_dist', 'insert_dist', 'mate_orientation', 'direction', 'length_bias', 'copy_bias', 'random_seed', 'desc_track' ],
        'ref_db': True,
        'genomics': False,
        'tech': ['sanger'],
        'variants': False,
        'ready': False
    },

    'metasim_genomics_illumina': {
        'title': 'MetaSim - Genomics Illumina',
        'caption': 'Generates synthetic reads that reflect the diverse taxonomical composition of typical metagenome data sets, allows the user to design a metagenome by specifying the number of genomes present at different levels of the NCBI taxonomy, and then to collect reads from the metagenome using a simulation of a number of different sequencing technologies.',
        'route': 'metasim_genomics_illumina',
        'arguments':[''],
        'ref_db': True,
        'genomics': True,
        'tech':['illumina'],
        'variants': True,
        'ready': False
    },

    'metasim_genomics_454': {
        'title': 'MetaSim - Genomics 454',
        'caption': 'Generates synthetic reads that reflect the diverse taxonomical composition of typical metagenome data sets, allows the user to design a metagenome by specifying the number of genomes present at different levels of the NCBI taxonomy, and then to collect reads from the metagenome using a simulation of a number of different sequencing technologies.',
        'route': 'metasim_genomics_454',
        'arguments':[''],
        'ref_db': True,
        'genomics': True,
        'tech':['454'],
        'variants': True,
        'ready': False
    },

    'metasim_genomics_sanger': {
        'title': 'MetaSim - Genomics Sanger',
        'caption': 'Generates synthetic reads that reflect the diverse taxonomical composition of typical metagenome data sets, allows the user to design a metagenome by specifying the number of genomes present at different levels of the NCBI taxonomy, and then to collect reads from the metagenome using a simulation of a number of different sequencing technologies.',
        'route': 'metasim_genomics_sanger',
        'arguments':[''],
        'ref_db': True,
        'genomics': True,
        'tech':['sanger'],
        'variants': True,
        'ready': False
    },

    'metasim_metagenomics_illumina': {
        'title': 'MetaSim - Metagenomics Illumina',
        'caption': 'Generates synthetic reads that reflect the diverse taxonomical composition of typical metagenome data sets, allows the user to design a metagenome by specifying the number of genomes present at different levels of the NCBI taxonomy, and then to collect reads from the metagenome using a simulation of a number of different sequencing technologies.',
        'route': 'metasim_metagenomics_illumina',
        'arguments':[''],
        'ref_db': True,
        'genomics': False,
        'tech':['illumina'],
        'variants': True,
        'ready': False
    },

    'metasim_metagenomics_454': {
        'title': 'MetaSim - Metagenomics 454',
        'caption': 'Generates synthetic reads that reflect the diverse taxonomical composition of typical metagenome data sets, allows the user to design a metagenome by specifying the number of genomes present at different levels of the NCBI taxonomy, and then to collect reads from the metagenome using a simulation of a number of different sequencing technologies.',
        'route': 'metasim_metagenomics_454',
        'arguments':[''],
        'ref_db': True,
        'genomics': False,
        'tech':['454'],
        'variants': True,
        'ready': False
    },
    
    'metasim_metagenomics_sanger': {
        'title': 'MetaSim - Metagenomics Sanger',
        'caption': 'Generates synthetic reads that reflect the diverse taxonomical composition of typical metagenome data sets, allows the user to design a metagenome by specifying the number of genomes present at different levels of the NCBI taxonomy, and then to collect reads from the metagenome using a simulation of a number of different sequencing technologies.',
        'route': 'metasim_metagenomics_sanger',
        'arguments':[''],
        'ref_db': True,
        'genomics': False,
        'tech':['sanger'],
        'variants': True,
        'ready': False
    },

    'nessm_illumina': {
        'title': 'NeSSM - Illumina',
        'caption': 'Next-generation Sequencing Simulator for Metagenomics, combining complete genomes currently available, a community composition table, and sequencing parameters, it can simulate metagenome sequencing better than existing systems.',
        'route': 'nessm_illumina',
        'arguments':[''],
        'ref_db': True,
        'genomics': False,
        'tech':['illumina'],
        'variants': False,
        'ready': False
    },

    'nessm_454': {
        'title': 'NeSSM - 454',
        'caption': 'Next-generation Sequencing Simulator for Metagenomics, combining complete genomes currently available, a community composition table, and sequencing parameters, it can simulate metagenome sequencing better than existing systems.',
        'route': 'nessm_454',
        'arguments':[''],
        'ref_db': True,
        'genomics': False,
        'tech':['454'],
        'variants': False,
        'ready': False
    },

    'readsim_nanopore': {
        'title': 'ReadSim - Nanopore',
        'caption': 'ReadSim is a fast and simple reads simulator to target long reads such as PacBio or Nanopore.',
        'route': 'readsim_nanopore',
        'arguments':[''],
        'ref_db': True,
        'genomics': True,
        'tech':['nanopore'],
        'variants': False,
        'ready': False
    },

    'readsim_pacbio': {
        'title': 'ReadSim - PacBio',
        'caption': 'ReadSim is a fast and simple reads simulator to target long reads such as PacBio or Nanopore.',
        'route': 'readsim_pacbio',
        'arguments':[''],
        'ref_db': True,
        'genomics': True,
        'tech':['pacbio'],
        'variants': False,
        'ready': False
    },

    'sinc': {
        'title': 'SInC',
        'caption': 'An accurate and fast error-model based simulator for SNPs, Indels and CNVs coupled with a read generator for short-read sequence data.',
        'route': 'sinc',
        'arguements':[],
        'ref_db': True,
        'genomics': True,
        'tech': ['illumina'],
        'variants': False,
        'ready': False
    },

    'simseq': {
        'title': 'SimSeq',
        'caption': 'An illumina paired-end and mate-pair short read simulator, attempts to model as many of the quirks that exist in Illumina data as possible. Some of these quirks include the potential for chimeric reads, and non-biotinylated fragment pull down in mate-pair libraries.',
        'route': 'simseq',
        'arguements':[],
        'ref_db': True,
        'genomics': True,
        'tech': ['illumina'],
        'variants': False,
        'ready': False
    },


    'simhtsd_454': {
        'title': 'simhtsd - 454',
        'caption': 'Given a reference sequence, simhtsd will create a large set of short nucleotide reads, simulating the output from today\'s high-throughput DNA sequencers, such as the Illumina Genome Analyzer II.',
        'route': 'simhtsd_454',
        'arguments': [ 'input', 'output', 'coverage', 'num_reads', 'generate_454', 'read_len', 'error_func', 'error_rate', 'incremental_error_rate', 'paired_end', 'distance_between_first_pos', 'std_dev' ],
        'ref_db': True,
        'genomics': True,
        'tech': ['454'],
        'variants': True,
        'ready': False
    },

    'simhtsd_illumina': {
        'title': 'simhtsd - Illumina',
        'caption': 'Given a reference sequence, simhtsd will create a large set of short nucleotide reads, simulating the output from today\'s high-throughput DNA sequencers, such as the Illumina Genome Analyzer II.',
        'route': 'simhtsd_illumina',
        'arguments': [ 'input', 'output', 'coverage', 'num_reads', 'generate_454', 'read_len', 'error_func', 'error_rate', 'incremental_error_rate', 'paired_end', 'distance_between_first_pos', 'std_dev' ],
        'ref_db': True,
        'genomics': True,
        'tech': ['illumina'],
        'variants': True,
        'ready': False
    },

    'simngs': {
        'title': 'simNGS',
        'caption': 'Simulating observations from Illumina sequencing machines using the statistical models behind the AYB base-calling software.',
        'route': 'simngs',
        'arguements':[],
        'ref_db': True,
        'genomics': True,
        'tech': ['illumina'],
        'variants': True,
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