from flask import render_template, flash, redirect, jsonify, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from app.simulators import SIMULATORS, sim_json
from app.forms import *
from app.tasks import create_and_start_job
from app.models import User, Job
from app import instance

"""
Unauthenticated Routes
"""

@instance.route('/')
def index():
    return render_template('index.html', title='Home', transparent_nav=True)

@instance.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()

    if form.validate_on_submit():
        user = User.objects(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid email or password', 'alert-danger')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)

        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('auth/login.html', title='Login', form=form)

@instance.route('/register', methods=['GET', 'POST'], strict_slashes=False)
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, institution=form.institution.data)
        user.set_password(form.password.data)
        user.save()
        flash('Congratulations, you are now a registered user!', 'alert-info')
        return redirect(url_for('login'))
    return render_template('auth/register.html', title='Register', form=form) 

@instance.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

"""
Authenticated Routes
"""
@instance.route('/dashboard', methods=['GET'], strict_slashes=False)
@login_required
def dashboard():
    jobs = Job.objects(user_id=current_user.id).order_by('-$natural').all()
    return render_template('dashboard.html', title='Dashboard', jobs=jobs)

@instance.route('/simulators/help', methods=['GET'], strict_slashes=False)
@login_required
def help():
    methods = [ 'IonTorrent', 'SOLiD', 'PacBio', '454', 'Illumina', 'Sanger', 'Nanopore' ]
    return render_template('help.html', title='Help', methods=methods)

@instance.route('/simulators', methods=['GET'], strict_slashes=False)
@login_required
def simulators():
    return render_template('cards.html', title='Cards', simulators=SIMULATORS)

"""
Simulator Routes
"""

@instance.route('/simulators/bear_parametric_abundance', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def bear_parametric_abundance():
    form = BearParametricAbundanceForm()
    if form.validate_on_submit():
        create_and_start_job('bear.parametric_abundance', form.name.data, { 'complexity' : form.complexity.data }, form.file.data)
        return redirect(url_for('dashboard'))
    return render_template('simulators/bear_parametric_abundance.html', title='Bear - Parametric Abundance', form=form)

@instance.route('/simulators/454sim', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def sim_454():
    form = Sim454Form()
    if form.validate_on_submit():
        create_and_start_job('454sim', form.name.data, { 
            'frag_count': form.frag_count.data, 
            'frag_length': form.frag_length.data, 
            'flow_simulation_count': form.flow_simulation_count.data, 
            'generation': form.generation.data
        }, form.file.data)
        return redirect(url_for('dashboard'))

    return render_template('simulators/454sim.html', title='454Sim', form=form)

@instance.route('/simulators/art454', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def art_454():
    form = Art454Form()
    if form.validate_on_submit():
        pass
        return redirect(url_for('dashboard'))
    return render_template('simulators/art454.html', title='ART 454', form=form)

@instance.route('/simulators/artsolid', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def art_solid():
    form = ArtSolidForm()
    if form.validate_on_submit():
        pass
        return redirect(url_for('dashboard'))
    return render_template('simulators/artsolid.html', title='ART SOLiD', form=form)

@instance.route('/simulators/artificial_fastq_generator', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def artificial_fastq_generator():
    form = ArtificialFastqGenerator()
    if form.validate_on_submit():
        pass
        return redirect(url_for('dashboard'))
    return render_template('simulators/artificial_fastq_generator.html', title='ArtificialFastqGenerator', form=form)

@instance.route('/simulators/curesim', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def curesim():
    form = CuresimForm()
    if form.validate_on_submit():
        pass
        return redirect(url_for('dashboard'))
    return render_template('simulators/curesim.html', title='CuReSim', form=form)

@instance.route('/simulators/dwgsim', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def dwgsim():
    form = DwgsimForm()
    if form.validate_on_submit():
        pass
        return redirect(url_for('dashboard'))
    return render_template('simulators/dwgsim.html', title='DWGSIM', form=form)

@instance.route('/simulators/eagle', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def eagle():
    form = EagleForm()
    if form.validate_on_submit():
        pass
        return redirect(url_for('dashboard'))
    return render_template('simulators/eagle.html', title='EAGLE', form=form)

@instance.route('/simulators/fastqsim', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def fastqsim():
    form = FastqsimForm()
    if form.validate_on_submit():
        pass
        return redirect(url_for('dashboard'))
    return render_template('simulators/fastqsim.html', title='FASTQSim', form=form)

@instance.route('/simulators/flowsim', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def flowsim():
    form = FlowsimForm()
    if form.validate_on_submit():
        pass
        return redirect(url_for('dashboard'))
    return render_template('simulators/flowsim.html', title='FlowSim', form=form)

@instance.route('/simulators/gemsim', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def gemsim():
    form = GemsimForm()
    if form.validate_on_submit():
        pass
        return redirect(url_for('dashboard'))
    return render_template('simulators/gemsim.html', title='GemSim', form=form)

@instance.route('/simulators/grinder', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def grinder():
    form = GrinderForm()
    if form.validate_on_submit():
        pass
        return redirect(url_for('dashboard'))
    return render_template('simulators/grinder.html', title='Grinder', form=form)

@instance.route('/simulators/mason', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def mason():
    form = MasonForm()
    if form.validate_on_submit():
        pass
        return redirect(url_for('dashboard'))
    return render_template('simulators/mason.html', title='Mason', form=form)

@instance.route('/simulators/metasim', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def metasim():
    form = MetasimForm()
    if form.validate_on_submit():
        pass
        return redirect(url_for('dashboard'))
    return render_template('simulators/metasim.html', title='MetaSim', form=form)

@instance.route('/simulators/nessm', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def nessm():
    form = NessmForm()
    if form.validate_on_submit():
        pass
        return redirect(url_for('dashboard'))
    return render_template('simulators/nessm.html', title='NeSSM', form=form)

@instance.route('/simulators/pbsim', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def pbsim():
    form = PbsimForm()
    if form.validate_on_submit():
        pass
        return redirect(url_for('dashboard'))
    return render_template('simulators/pbsim.html', title='Pbsim', form=form)

@instance.route('/simulators/readsim', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def readsim():
    form = ReadsimForm()
    if form.validate_on_submit():
        pass
        return redirect(url_for('dashboard'))
    return render_template('simulators/readsim.html', title='ReadSim', form=form)

@instance.route('/simulators/sinc', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def sinc():
    form = SincForm()
    if form.validate_on_submit():
        pass
        return redirect(url_for('dashboard'))
    return render_template('simulators/sinc.html', title='SInC', form=form)

@instance.route('/simulators/simseq', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def simseq():
    form = SimseqForm()
    if form.validate_on_submit():
        pass
        return redirect(url_for('dashboard'))
    return render_template('simulators/simseq.html', title='SimSeq', form=form)

@instance.route('/simulators/simhtsd', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def simhtsd():
    form = SimhtsdForm()
    if form.validate_on_submit():
        pass
        return redirect(url_for('dashboard'))
    return render_template('simulators/simhtsd.html', title='Simhtsd', form=form)

@instance.route('/simulators/pirs', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def pirs():
    form = PirsForm()
    if form.validate_on_submit():
        pass
        return redirect(url_for('dashboard'))
    return render_template('simulators/pirs.html', title='pIRS', form=form)

@instance.route('/simulators/simngs', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def simngs():
    form = SimngsForm()
    if form.validate_on_submit():
        pass
        return redirect(url_for('dashboard'))
    return render_template('simulators/simngs.html', title='simNGS', form=form)

@instance.route('/simulators/wgsim', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def wgsim():
    form = WgsimForm()
    if form.validate_on_submit():
        pass
        return redirect(url_for('dashboard'))
    return render_template('simulators/wgsim.html', title='wgsim', form=form)

@instance.route('/simulators/xs', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def xs():
    form = XsForm()
    if form.validate_on_submit():
        pass
        return redirect(url_for('dashboard'))
    return render_template('simulators/xs.html', title='xs', form=form)

"""
API Routes
"""

@instance.route('/api/users', methods=['GET'], strict_slashes=False)
def get_users():
    return User.objects.all().to_json()

@instance.route('/api/jobs', methods=['GET'], strict_slashes=False)
def get_jobs():
    return Job.objects.all().to_json()

@instance.route('/api/simulators', methods=['GET'], strict_slashes=False)
def get_simulators():
    return jsonify(sim_json())