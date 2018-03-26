$('input[type=file]').on('change', function() {
    var fileName = $(this).val();
    $(this).next('.custom-file-label').html(fileName);
});

$('input.js-help-tree').on('change', function() {

    // Instantiate the object to store values.
    if (!window.helpTree) {
        window.helpTree = {};
    }

    var key = $(this)[0].name;
    var value = $(this).val().toLowerCase();
    window.helpTree[key] = value;

    $('input.organism-input').prop('disabled', false);
    $('input.genome-input').prop('disabled', false);

    if (window.helpTree['ref-seq'] === 'no') {
        $('input.organism-input').prop('disabled', true);
        $('input.genome-input').prop('disabled', true);
        $('.nanopore-input, .pacbio-input, .sanger-input').prop('disabled', true);
    } else if (window.helpTree['ref-seq'] && window.helpTree['organisms'] && window.helpTree['variants']) {
        var organisms = window.helpTree['organisms'];
        var variants = window.helpTree['variants'];

        var methodTree = {
            'one': {
                'yes': [ 'nanopore' ],
                'no': []
            },
            'several': {
                'yes': [ 'iontorrent', 'solid', 'pacbio', 'nanopore' ],
                'no': [ 'nanopore' ]
            }
        };

        var methodString = methodTree[organisms][variants].map(function(m) {
            return '.' + m + '-input'
        }).join(', ');
        $('input.method-input').prop('disabled', false);
        $(methodString).prop('disabled', true);
    }

    renderHelpTreeResults(window.helpTree)
});

function renderHelpTreeResults(results) {
    // Hide all results first.
    $('.js-help-tree-result').prop('hidden', true);

    // Render in the simulators that correspond with the results.
    if (!results['method']) {
        // If there is no selected method/technology, then render all the simulators.
        $('.js-help-tree-result').prop('hidden', false);
    } else if (results['ref-seq'] === 'no') {
        $('.js-help-tree-result#xs').prop('hidden', false);
    } else if (results['ref-seq'] && results['organisms'] && results['variants'] && results['method']) {

        var resultTree = {
            'one': {
                'yes': {
                    'iontorrent': [ 'curesim' ],
                    'solid':      [ 'art', 'curesim' ],
                    'pacbio':     [ 'pbsim' ],
                    'sanger':     [ 'metasim' ],
                    'illumina':   [ 'art', 'artificialfastqgenerator', 'curesim', 'metasim', 'simhtsd', 'simngs' ],
                    '454':        [ '454sim', 'art', 'curesim', 'flowsim', 'metasim', 'simhtsd' ]
                },
                'no': {
                    '454':        [ 'bear', 'eagle', 'gemsim', 'grinder', 'mason' ],
                    'sanger':     [ 'grinder', 'mason' ],
                    'solid':      [ 'dwgsim', 'fastqsim', 'wgsim' ],
                    'iontorrent': [ 'bear', 'eagle', 'dwgsim', 'fastqsim' ],
                    'nanopore':   [ 'readsim' ],
                    'illumina':   [ 'bear', 'dwgsim', 'eagle', 'fastqsim', 'gemsim', 'grinder', 'mason', 'pirs', 'simseq', 'sinc', 'wgsim' ],
                    'pacbio':     [ 'eagle', 'fastqsim', 'readsim' ]
                },
            },
            'several': {
                'yes': {
                    'illumina': [ 'metasim' ],
                    '454':      [ 'metasim' ],
                    'sanger':   [ 'metasim' ],
                },
                'no': {
                    'pacbio':     [ 'fastqsim' ],
                    'solid':      [ 'fastqsim' ],
                    'sanger':     [ 'grinder' ],
                    'illumina':   [ 'bear', 'fastqsim', 'gemsim', 'grinder', 'mason', 'nessm', 'pirs' ],
                    'iontorrent': [ 'bear', 'fastqsim' ],
                    '454':        [ 'bear', 'gemsim', 'grinder', 'mason', 'nessm' ]
                }
            }
        };

        try {
            var resultString = resultTree[results['organisms']][results['variants']][results['method']].map(function(r) {
                return '.js-help-tree-result#' + r;
            }).join(', ');
            $(resultString).prop('hidden', false);
        } catch(e) {
            $('.js-help-tree-result').prop('hidden', false);
        }
    } else {
        // For all other cases, show all simulators.
        $('.js-help-tree-result').prop('hidden', false);
    }
}