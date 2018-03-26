$('input[type=file]').on('change', function() {
    var fileName = $(this).val();
    $(this).next('.custom-file-label').html(fileName);
});

$('input.help-tree').on('change', function() {

    // Instantiate the object to store values.
    if (!window.helpTree) {
        window.helpTree = {};
    }

    var key = $(this)[0].name;
    var value = $(this).val();
    window.helpTree[key] = value;

    if (key === 'ref-seq' && value === 'no') {
        $('input.organism-input').prop('disabled', true);
        $('input.genome-input').prop('disabled', true);
        $('.nanopere-input, .pacbio-input, .sanger-input').prop('disabled', true);
    } else if (window.helpTree['ref-seq'] && window.helpTree['organisms'] && window.helpTree['variants']) {
        var organisms = window.helpTree['organisms'];
        var variants = window.helpTree['variants'];

        var methodTree = {
            'one': {
                'yes': [ 'nanopere' ],
                'no': []
            },
            'several': {
                'yes': [ 'iontorrent', 'solid', 'pacbio', 'nanopere' ],
                'no': [ 'nanopere' ]
            }
        };

        var methodString = methodTree[organisms][variants].map(function(m) {
            return '.' + m + '-input'
        }).join(', ');
        $('input.method-input').prop('disabled', false);
        $(methodString).prop('disabled', true)
    } else {
        $('input.method-input').prop('disabled', false);
    }
});