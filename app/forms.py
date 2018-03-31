from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField, DecimalField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, NumberRange, Optional
from app.models import User

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

class BearParametricAbundanceForm(BaseSimulatorForm):
    complexity = SelectField('Complexity', choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], validators=[DataRequired()])

class Sim454Form(BaseSimulatorForm):
    generation = SelectField('Generation', choices=[('Ti', 'Ti'), ('GS', 'GS'), ('FLX', 'FLX')], validators=[DataRequired()])
    flow_simulation_count = IntegerField('Flow Simulation Count', validators=[NumberRange(min=1, max=2000000)])
    frag_length = IntegerField('Fragment Length', validators=[NumberRange(min=1, max=2000000)])
    frag_count = IntegerField('Fragment Count', validators=[NumberRange(min=1, max=2000000)])

class Art454Form(BaseSimulatorForm):
    fold_coverage = IntegerField('Flow Coverage', validators=[NumberRange(min=1, max=1000000)])
    mean_frag_len = IntegerField('Mean Fragment Length (For Paired End Reads)', validators=[Optional()])
    std_dev = DecimalField('Standard Deviation (For Paired End Reads)', validators=[Optional()])
    random_seed = IntegerField('Random Seed', validators=[Optional()])

class ArtSolidForm(BaseSimulatorForm):
    read_len = IntegerField('Read Length') 
    fold_coverage = IntegerField('Fold Coverage') 

class ArtificialFastqGenerator(BaseSimulatorForm):
    pass

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