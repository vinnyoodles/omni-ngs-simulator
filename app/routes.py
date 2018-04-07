import os, arc, mailer
from flask import render_template, flash, redirect, jsonify, url_for, request, send_file
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

@instance.route('/simulators/help/tree', methods=['GET'], strict_slashes=False)
@login_required
def help_tree():
    return render_template('tree.html', title='Help')

@instance.route('/simulators', methods=['GET'], strict_slashes=False)
@login_required
def simulators():
    return render_template('cards.html', title='Cards', simulators=SIMULATORS)

@instance.route('/download/<job_id>', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def download(job_id):
    client = arc.Client('newriver2.arc.vt.edu', arc.ARC_USER)
    local_path = os.path.join('/tmp', 'output.tar.gz')
    remote_path = os.path.join(arc.ARC_DIR, job_id, 'output.tar.gz')
    client.get_file(local_path, remote_path)
    client.close()
    return send_file(local_path)

"""
Simulator Routes
"""

def base_simulator_route(simulator, title, FormClass):
    form = FormClass()
    if form.validate_on_submit():
        create_and_start_job(simulator, form)
        return redirect(url_for('dashboard'))
    return render_template('simulators/{}.html'.format(simulator), title=title, form=form)

@instance.route('/simulators/454sim', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def sim_454():
    return base_simulator_route('454sim', '454Sim', Sim454Form)

@instance.route('/simulators/art454', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def art_454():
    return base_simulator_route('art_454', 'ART 454', Art454Form)

@instance.route('/simulators/artsolid', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def art_solid():
    return base_simulator_route('art_solid', 'ART SOLiD', ArtSolidForm)

@instance.route('/simulators/artificial_fastq_generator', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def artificial_fastq_generator():
    return base_simulator_route('artificialfastqgenerator', 'ArtificialFastqGenerator', ArtificialFastqGeneratorForm)

@instance.route('/simulators/curesim', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def curesim():
    return base_simulator_route('curesim', 'CuReSim', CuresimForm)

@instance.route('/simulators/dwgsim', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def dwgsim():
    return base_simulator_route('dwgsim', 'DWGSIM', DwgsimForm)

@instance.route('/simulators/eagle', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def eagle():
    return base_simulator_route('eagle', 'EAGLE', EagleForm)

@instance.route('/simulators/fastqsim', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def fastqsim():
    return base_simulator_route('fastqsim', 'FASTQSim', FastqsimForm)

@instance.route('/simulators/flowsim', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def flowsim():
    return base_simulator_route('flowsim', 'FlowSim', FlowsimForm)

@instance.route('/simulators/gemsim', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def gemsim():
    return base_simulator_route('gemsim', 'GemSim', GemsimForm)

@instance.route('/simulators/grinder', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def grinder():
    return base_simulator_route('grinder', 'Grinder', GrinderForm)

@instance.route('/simulators/mason_sanger', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def mason_sanger():
    return base_simulator_route('mason_sanger', 'Mason - Sanger', MasonSangerForm)

@instance.route('/simulators/mason_illumina', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def mason_illumina():
    return base_simulator_route('mason_illumina', 'Mason - Illumina', MasonIlluminaForm)

@instance.route('/simulators/metasim', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def metasim():
    return base_simulator_route('metasim', 'MetaSim', MetasimForm)

@instance.route('/simulators/nessm', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def nessm():
    return base_simulator_route('nessm', 'NeSSM', NessmForm)

@instance.route('/simulators/pbsim', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def pbsim():
    return base_simulator_route('pbsim', 'Pbsim', PbsimForm)

@instance.route('/simulators/readsim', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def readsim():
    return base_simulator_route('readsim', 'ReadSim', ReadsimForm)

@instance.route('/simulators/sinc', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def sinc():
    return base_simulator_route('sinc', 'SInC', SincForm)

@instance.route('/simulators/simseq', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def simseq():
    return base_simulator_route('simseq', 'SimSeq', SimseqForm)

@instance.route('/simulators/simhtsd', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def simhtsd():
    return base_simulator_route('simhtsd', 'Simhtsd', SimhtsdForm)

@instance.route('/simulators/pirs', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def pirs():
    return base_simulator_route('pirs', 'pIRS', PirsForm)

@instance.route('/simulators/simngs', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def simngs():
    return base_simulator_route('simngs', 'simNGS', SimngsForm)

@instance.route('/simulators/wgsim', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def wgsim():
    return base_simulator_route('wgsim', 'wgsim', WgsimForm)

@instance.route('/simulators/xs', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def xs():
    return base_simulator_route('xs', 'xs', XsForm)

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

@instance.route('/api/jobs/started/<job_id>', methods=['POST'], strict_slashes=False)
def started_job(job_id):
    command = request.json['command']
    job = Job.objects(id=job_id).first()
    job.status = 'started'
    job.command = command
    job.save()
    return jsonify({ 'message' : 'ok' })

@instance.route('/api/jobs/finished/<job_id>', methods=['POST'], strict_slashes=False)
def finished_job(job_id):
    job = Job.objects(id=job_id).first()
    job.status = 'finished'
    job.save()

    user = User.objects(id=job.user_id).first()
    mailer.notify(job, user)

    return jsonify({ 'message' : 'ok' })