import sys
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField, DecimalField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, NumberRange, Optional
from app.models import User
from random import *

RAND_SEED_MAX = 1000000000

def rand_seed():
    return randint(1, RAND_SEED_MAX)

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    institution = StringField('Institution', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_email(self, email):
        user = User.objects(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class BaseSimulatorForm(FlaskForm):
    name = StringField('Name')
    file = FileField('Input File', validators=[FileRequired()])
    submit = SubmitField('Submit')

class Sim454Form(BaseSimulatorForm):
    generation = SelectField('Generation', choices=[('Ti', 'Ti'), ('GS', 'GS'), ('FLX', 'FLX')], validators=[DataRequired()])
    flow_simulation_count = IntegerField('Flow Simulation Count', validators=[NumberRange(min=1, max=2000000)])
    frag_length = IntegerField('Fragment Length', validators=[NumberRange(min=1, max=2000000)])
    frag_count = IntegerField('Fragment Count', validators=[NumberRange(min=1, max=RAND_SEED_MAX)])

class Art454Form(BaseSimulatorForm):
    fold_coverage = IntegerField('Fold Coverage', validators=[NumberRange(min=1, max=1000000)])
    mean_frag_len = IntegerField('Mean Fragment Length (For Paired End Reads)', validators=[Optional()])
    std_dev = DecimalField('Standard Deviation (For Paired End Reads)', validators=[Optional()])
    random_seed = IntegerField('Random Seed', validators=[DataRequired(), NumberRange(min=1, max=RAND_SEED_MAX)])
    simulation_type = SelectField('Simulation Type', choices=[('1', 'Single End'), ('2', 'Paired Ends')], validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        super(Art454Form, self).__init__(*args, **kwargs)
        self.random_seed.data = rand_seed()

class ArtSolidForm(BaseSimulatorForm):
    read_len = IntegerField('Read Length', validators=[DataRequired(), NumberRange(min=1, max=2000000)])
    simulation_type = SelectField('Simulation Type', choices=[('1', 'Single End'), ('2', 'Paired Ends')], validators=[DataRequired()])
    random_seed = IntegerField('Random Seed', validators=[DataRequired(), NumberRange(min=1, max=RAND_SEED_MAX)])
    fold_coverage = IntegerField('Fold Coverage', validators=[NumberRange(min=1, max=1000000)])
    mean_frag_len = IntegerField('Mean Fragment Length (For Paired End Reads)', validators=[Optional()])
    std_dev = DecimalField('Standard Deviation (For Paired End Reads)', validators=[Optional()])

    def __init__(self, *args, **kwargs):
        super(ArtSolidForm, self).__init__(*args, **kwargs)
        self.random_seed.data = rand_seed()

class ArtificialFastqGeneratorForm(BaseSimulatorForm):
    sequence_identifier = StringField('Sequence Identifier in reference where read generation will begin (Must begin with a >)')
    coverage_mean = DecimalField('Spread of Coverage Mean', default=0.22)
    peak_coverage_mean = DecimalField('Peak Coverage Mean', default=37.7)
    gc_content_peak = DecimalField('GC Content for Regions with Peak Coverage Mean', default=0.45)
    coverage_std_dev = DecimalField('Coverage Standard Deviation divided by the mean', default=0.2)
    read_length = IntegerField('Read Length', default=76)
    mean_length = IntegerField('Mean DNA Template Length', default=210)
    std_dev = IntegerField('Standard Deviation of the DNA Template Length', default=60)

class CuresimForm(BaseSimulatorForm):
    read_count = IntegerField('Number of Reads to Generate', default=50000, validators=[DataRequired()])
    read_mean = IntegerField('Read Mean Size', default=200, validators=[DataRequired()])
    read_size_std_dev = DecimalField('Standard Deviation for Read Size', default=20.0, validators=[DataRequired()])
    random_read_count = IntegerField('Number of Random Reads', default=0, validators=[DataRequired()])
    deletion_rate = DecimalField('Deletion Rate', default=0.01, validators=[DataRequired(), NumberRange(min=0, max=1)])
    insertion_rate = DecimalField('Insertion Rate', default=0.005, validators=[DataRequired(), NumberRange(min=0, max=1)])
    substitution_rate = DecimalField('Substitution Rate', default=0.005, validators=[DataRequired(), NumberRange(min=0, max=1)])

class DwgsimForm(BaseSimulatorForm):
    pair_outer_distance = IntegerField('Outer distance between two ends for pairs', default=500, validators=[DataRequired()])
    distance_std_dev = IntegerField('Standard Deviation of the Distance for Pairs', default=50, validators=[DataRequired()])
    mean_coverage = DecimalField('Mean coverage across available positions', default=100, validators=[DataRequired()])
    mutation_rate = DecimalField('Mutation Rate', default=0.001, validators=[DataRequired(), NumberRange(min=0, max=1)])
    mutation_frequency = DecimalField('Somatic Mutation Rate', default=0.5, validators=[DataRequired(), NumberRange(min=0, max=1)])
    mutation_indel_percentage = DecimalField('Indel Mutation Probability', default=0.1, validators=[DataRequired(), NumberRange(min=0, max=1)])
    indel_extension_rate = DecimalField('Indel Extension Probability', default=0.3, validators=[DataRequired(), NumberRange(min=0, max=1)])

    min_indel_length = IntegerField('Indel Extension Probability', default=1, validators=[DataRequired()])
    random_read_probability = DecimalField('Indel Extension Probability', default=0.05, validators=[DataRequired(), NumberRange(min=0, max=1)])
    technology = SelectField('Technology', choices=[('0', 'Illumina'), ('1', 'SOLiD'), ('2', 'Ion Torrent')], validators=[DataRequired()])
    random_seed = IntegerField('Random Seed', validators=[DataRequired(), NumberRange(min=1, max=RAND_SEED_MAX)])

    def __init__(self, *args, **kwargs):
        super(DwgsimForm, self).__init__(*args, **kwargs)
        self.random_seed.data = rand_seed()

class EagleForm(BaseSimulatorForm):
    pass

class FastqsimForm(BaseSimulatorForm):
    pass

class FlowsimForm(BaseSimulatorForm):
    pass

class GemsimForm(BaseSimulatorForm):
    pass

class GrinderForm(BaseSimulatorForm):
    total_reads = IntegerField('Number of reads to generate')
    read_dist = IntegerField('Read length distribution')
    insert_dist = IntegerField('Reads spanning the given insert length')
    mate_orientation = SelectField('Orientation of paired-end or mate-pair reads', choices=[('FR', 'Forward Reverse'), ('FF', 'Forward Forward'), ('RF', 'Reverse Forward'), ('RR', 'Reverse Reverse')])
    direction = SelectField('Read direction', choices=[('0', 'Bidirectional'), ('1', 'Unidirectional'), ('-1', 'Reverse')])
    length_bias = BooleanField('Sample sequences proportionally to their length')
    copy_bias = BooleanField('Sample sequences proportionally to the number of copies of the target gene')
    random_seed = IntegerField('Random Seed', validators=[DataRequired(), NumberRange(min=1, max=RAND_SEED_MAX)])
    desc_track = BooleanField('Track read information as description')

    def __init__(self, *args, **kwargs):
        super(GrinderForm, self).__init__(*args, **kwargs)
        self.random_seed.data = rand_seed()

class MasonSangerForm(BaseSimulatorForm):
    read_count = IntegerField('Number of reads to simulate', default=1000, validators=[DataRequired(), NumberRange(min=1, max=2000000)])
    random_source_sequence_length = IntegerField('Length of random source sequence', default=1000000, validators=[DataRequired(), NumberRange(min=1, max=2000000)])
    a_probability = DecimalField('Probability for A in random sequence', default=0.25, validators=[DataRequired(), NumberRange(min=0, max=1)])
    c_probability = DecimalField('Probability for C in random sequence', default=0.25, validators=[DataRequired(), NumberRange(min=0, max=1)])
    g_probability = DecimalField('Probability for G in random sequence', default=0.25, validators=[DataRequired(), NumberRange(min=0, max=1)])

    mismatch_begin_probability = DecimalField('Probability for a mismatch to begin', default=0.005, validators=[DataRequired(), NumberRange(min=0, max=1)])
    mismatch_end_probability = DecimalField('Probability for a mismatch to end', default=0.01, validators=[DataRequired(), NumberRange(min=0, max=1)])
    insertion_begin_probability = DecimalField('Probability for a insertion to begin', default=0.0025, validators=[DataRequired(), NumberRange(min=0, max=1)])
    insertion_end_probability = DecimalField('Probability for a insertion to end', default=0.005, validators=[DataRequired(), NumberRange(min=0, max=1)])
    deletion_begin_probability = DecimalField('Probability for a deletion to begin', default=0.0025, validators=[DataRequired(), NumberRange(min=0, max=1)])
    deletion_end_probability = DecimalField('Probability for a deletion to end', default=0.005, validators=[DataRequired(), NumberRange(min=0, max=1)])
    random_seed = IntegerField('Random Seed', validators=[DataRequired(), NumberRange(min=1, max=RAND_SEED_MAX)])

    def __init__(self, *args, **kwargs):
        super(MasonSangerForm, self).__init__(*args, **kwargs)
        self.random_seed.data = rand_seed()

class MasonIlluminaForm(BaseSimulatorForm):
    read_count = IntegerField('Number of reads to simulate', default=1000, validators=[DataRequired(), NumberRange(min=1, max=2000000)])
    random_source_sequence_length = IntegerField('Length of random source sequence', default=1000000, validators=[DataRequired(), NumberRange(min=1, max=2000000)])
    a_probability = DecimalField('Probability for A in random sequence', default=0.25, validators=[DataRequired(), NumberRange(min=0, max=1)])
    c_probability = DecimalField('Probability for C in random sequence', default=0.25, validators=[DataRequired(), NumberRange(min=0, max=1)])
    g_probability = DecimalField('Probability for G in random sequence', default=0.25, validators=[DataRequired(), NumberRange(min=0, max=1)])

    insertion_probability = DecimalField('Probability of an insertion', default=0.001, validators=[DataRequired(), NumberRange(min=0, max=1)])
    deletion_probability = DecimalField('Probability of a deletion', default=0.001, validators=[DataRequired(), NumberRange(min=0, max=1)])
    avg_mismatch_probability = DecimalField('Average Mismatch Probability', default=0.004, validators=[DataRequired(), NumberRange(min=0, max=1)])
    first_base_mismatch_probability = DecimalField('Probability of a mismatch at the first base', default=0.002, validators=[DataRequired(), NumberRange(min=0, max=1)])
    last_base_mismatch_probability = DecimalField('Probability of a mismatch at the last base', default=0.012, validators=[DataRequired(), NumberRange(min=0, max=1)])
    random_seed = IntegerField('Random Seed', validators=[DataRequired(), NumberRange(min=1, max=RAND_SEED_MAX)])

    def __init__(self, *args, **kwargs):
        super(MasonIlluminaForm, self).__init__(*args, **kwargs)
        self.random_seed.data = rand_seed()


class MetasimForm(BaseSimulatorForm):
    pass

class NessmForm(BaseSimulatorForm):
    pass

class PbsimForm(BaseSimulatorForm):
    min_length = IntegerField('Minimum length', default=100, validators=[DataRequired(), NumberRange(min=1, max=2000000)])
    max_length = IntegerField('Maximum length', default=25000, validators=[DataRequired(), NumberRange(min=1, max=2000000)])
    min_accuracy = DecimalField('Minimum accuracy', default=0.75, validators=[DataRequired()])
    max_accuracy = DecimalField('Maximum accuracy', default=1, validators=[DataRequired()])
    substition_percentage = DecimalField('Substitution percentage', default=0.1, validators=[DataRequired(), NumberRange(min=0, max=1)])
    insertion_percentage = DecimalField('Insertion percentage', default=0.6, validators=[DataRequired(), NumberRange(min=0, max=1)])
    deletion_percentage = DecimalField('Deletion percentage', default=0.3, validators=[DataRequired(), NumberRange(min=0, max=1)])
    random_seed = IntegerField('Random Seed', validators=[DataRequired(), NumberRange(min=1, max=RAND_SEED_MAX)])
    fastq_file = FileField('Sample Fastq File', validators=[FileRequired()])

    def __init__(self, *args, **kwargs):
        super(PbsimForm, self).__init__(*args, **kwargs)
        self.random_seed.data = rand_seed()

class ReadsimForm(BaseSimulatorForm):
    pass

class SincForm(BaseSimulatorForm):
    pass

class SimseqForm(BaseSimulatorForm):
    pass

class SimhtsdForm(BaseSimulatorForm):
    coverage = IntegerField('Desired coverage')
    num_reads = IntegerField('Number of reads to output')
    generate_454 = BooleanField('Generate 454 style data')
    read_len = IntegerField('Read length')
    error_func = BooleanField('Turn on error function')
    error_rate = DecimalField('Starting error rate')
    incremental_error_rate = DecimalField('Incremental error rate per position')
    paired_end = BooleanField('Paired end run')
    distance_between_first_pos = IntegerField('Distance between first position of each sequence')
    std_dev = IntegerField('Standard deviation of distances')


class PirsForm(BaseSimulatorForm):
    read_len = IntegerField('Length of generated reads', default=100, validators=[DataRequired(), NumberRange(min=1, max=2000000)])
    coverage = IntegerField('Average sequencing coverage (depth)', default=200, validators=[DataRequired(), NumberRange(min=1, max=2000000)])
    insertion_len = IntegerField('Average length of generated insertion', default=100, validators=[DataRequired(), NumberRange(min=1, max=2000000)])
    std_dev_insertion_len = DecimalField('Standard deviation of insertion length', default=0.1, validators=[DataRequired()])
    random_seed = IntegerField('Random Seed', validators=[DataRequired(), NumberRange(min=1, max=RAND_SEED_MAX)])

    def __init__(self, *args, **kwargs):
        super(PirsForm, self).__init__(*args, **kwargs)
        self.random_seed.data = rand_seed()

class SimngsForm(BaseSimulatorForm):
    pass

class WgsimForm(BaseSimulatorForm):
    base_error_rate = DecimalField('Base error rate', default=0.02, validators=[DataRequired(), NumberRange(min=0, max=1)])
    outer_distance = IntegerField('Outer distance between two ends', default=500, validators=[DataRequired()])
    std_dev = IntegerField('Standard Deviation', default=50, validators=[DataRequired()])
    read_pair_count = IntegerField('Number of read pairs', default=1000000, validators=[DataRequired()])
    first_read_len = IntegerField('Length of the first read', default=70, validators=[DataRequired()])
    second_read_len = IntegerField('Length of the second read', default=70, validators=[DataRequired()])
    mutation_rate = DecimalField('Mutation rate', default=0.001, validators=[DataRequired(), NumberRange(min=0, max=1)])
    indel_fraction = DecimalField('Indel percentage', default=0.15, validators=[DataRequired()])
    indel_extension_rate = DecimalField('Probability of indel extension', default=0.30, validators=[DataRequired(), NumberRange(min=0, max=1)])
    random_seed = IntegerField('Random Seed', validators=[DataRequired(), NumberRange(min=1, max=RAND_SEED_MAX)])

    def __init__(self, *args, **kwargs):
        super(WgsimForm, self).__init__(*args, **kwargs)
        self.random_seed.data = rand_seed()

class XsForm(FlaskForm):
    technology = SelectField('Technology', choices=[('1', '454'), ('2', 'Illumina'), ('3', 'SOLiD'), ('4', 'Ion Torrent')], validators=[DataRequired()])
    header_format = SelectField('Header format', choices=[('1', 'Length appendix'), ('2', 'Pair end')], validators=[DataRequired()])
    read_per_file = IntegerField('Number of reads per file', default=100, validators=[DataRequired()])
    a_probability = DecimalField('Frequency of A', default=0.20, validators=[DataRequired(), NumberRange(min=0, max=1)])
    c_probability = DecimalField('Frequency of C', default=0.20, validators=[DataRequired(), NumberRange(min=0, max=1)])
    g_probability = DecimalField('Frequency of G', default=0.20, validators=[DataRequired(), NumberRange(min=0, max=1)])
    t_probability = DecimalField('Frequency of T', default=0.20, validators=[DataRequired(), NumberRange(min=0, max=1)])
    n_probability = DecimalField('Frequency of N', default=0.20, validators=[DataRequired(), NumberRange(min=0, max=1)])
    repeat_count = IntegerField('Number of repeats', default=0, validators=[DataRequired()])
    repeat_min = IntegerField('Minimum repeat size', default=0, validators=[DataRequired()])
    repeat_max = IntegerField('Maximum repeat size', default=0, validators=[DataRequired()])
    mutation_frequency = DecimalField('Mutation rate', default=0.001, validators=[DataRequired(), NumberRange(min=0, max=1)])
    random_seed = IntegerField('Random Seed', validators=[DataRequired(), NumberRange(min=1, max=RAND_SEED_MAX)])

    name = StringField('Name')
    submit = SubmitField('Submit')

    def __init__(self, *args, **kwargs):
        super(XsForm, self).__init__(*args, **kwargs)
        self.random_seed.data = rand_seed()