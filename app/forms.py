import sys
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField, DecimalField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, NumberRange, Optional
from app.models import User
from random import *

def rand_seed():
    return randint(1, 1000000000)

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
    frag_count = IntegerField('Fragment Count', validators=[NumberRange(min=1, max=2000000)])

class Art454Form(BaseSimulatorForm):
    fold_coverage = IntegerField('Fold Coverage', validators=[NumberRange(min=1, max=1000000)])
    mean_frag_len = IntegerField('Mean Fragment Length (For Paired End Reads)', validators=[Optional()])
    std_dev = DecimalField('Standard Deviation (For Paired End Reads)', validators=[Optional()])
    random_seed = IntegerField('Random Seed', validators=[DataRequired(), NumberRange(min=1, max=2000000)])
    simulation_type = SelectField('Simulation Type', choices=[('1', 'Single End'), ('2', 'Paired Ends')], validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        super(Art454Form, self).__init__(*args, **kwargs)
        self.random_seed.data = rand_seed()

class ArtSolidForm(BaseSimulatorForm):
    read_len = IntegerField('Read Length', validators=[DataRequired(), NumberRange(min=1, max=2000000)])
    fold_coverage = IntegerField('Fold Coverage', validators=[NumberRange(min=1, max=1000000)])
    mean_frag_len = IntegerField('Mean Fragment Length (For Paired End Reads)', validators=[Optional()])
    std_dev = DecimalField('Standard Deviation (For Paired End Reads)', validators=[Optional()])
    random_seed = IntegerField('Random Seed', validators=[DataRequired(), NumberRange(min=1, max=2000000)])
    simulation_type = SelectField('Simulation Type', choices=[('1', 'Single End'), ('2', 'Paired Ends')], validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        super(ArtSolidForm, self).__init__(*args, **kwargs)
        self.random_seed.data = rand_seed()

class ArtificialFastqGenerator(BaseSimulatorForm):
    sequence_identifier = StringField('Sequence Identifier in reference where read generation will begin')
    coverage_mean = DecimalField('Spread of Coverage Mean', default=0.22)
    peak_coverage_mean = DecimalField('Peak Coverage Mean', default=37.7)
    gc_content_peak = DecimalField('GC Content for Regions with Peak Coverage Mean', default=0.45)
    coverage_std_dev = DecimalField('Coverage Standard Deviation divided by the mean', default=0.2)
    read_length = IntegerField('Read Length', default=76)
    mean_length = IntegerField('Mean DNA Template Length', default=210)
    std_dev = IntegerField('Standard Deviation of the DNA Template Length', default=60)

class CuresimForm(BaseSimulatorForm):
    pass

class DwgsimForm(BaseSimulatorForm):
    pass

class EagleForm(BaseSimulatorForm):
    pass

class FastqsimForm(BaseSimulatorForm):
    pass

class FlowsimForm(BaseSimulatorForm):
    pass

class GemsimForm(BaseSimulatorForm):
    pass

class GrinderForm(BaseSimulatorForm):
    pass

class MasonForm(BaseSimulatorForm):
    pass

class MetasimForm(BaseSimulatorForm):
    pass

class NessmForm(BaseSimulatorForm):
    pass

class PbsimForm(BaseSimulatorForm):
    pass

class ReadsimForm(BaseSimulatorForm):
    pass

class SincForm(BaseSimulatorForm):
    pass

class SimseqForm(BaseSimulatorForm):
    pass

class SimhtsdForm(BaseSimulatorForm):
    pass

class PirsForm(BaseSimulatorForm):
    pass

class SimngsForm(BaseSimulatorForm):
    pass

class WgsimForm(BaseSimulatorForm):
    pass

class XsForm(BaseSimulatorForm):
    pass