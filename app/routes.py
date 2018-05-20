import os, arc, mailer
from flask import render_template, flash, redirect, jsonify, url_for, request, send_file
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from mongoengine.queryset.visitor import Q
from functools import reduce

from app.simulators import SIMULATORS, sim_json
from app.forms import *
from app.tasks import create_and_start_job
from app.models import User, Job
from app import instance

PROD_ENV = os.environ.get('PROD_ENV') == '1'

def prefix_url_for(route, **kwargs):
    url = url_for(route, **kwargs)
    prefix = ''
    if PROD_ENV:
        prefix = '/omningssimulator'
    return prefix + url

"""
Unauthenticated Routes
"""

@instance.route('/', strict_slashes=False)
def index():
    return render_template('index.html', title='Home', transparent_nav=True, prefix_url_for=prefix_url_for)

@instance.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    if current_user.is_authenticated:
        return redirect(prefix_url_for('index'))
    form = LoginForm()

    if form.validate_on_submit():
        user = User.objects(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid email or password', 'alert-danger')
            return redirect(prefix_url_for('login'))
        login_user(user, remember=form.remember_me.data)

        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = prefix_url_for('index')
        return redirect(next_page)
    return render_template('auth/login.html', title='Login', form=form, prefix_url_for=prefix_url_for)

@instance.route('/register', methods=['GET', 'POST'], strict_slashes=False)
def register():
    if current_user.is_authenticated:
        return redirect(prefix_url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, institution=form.institution.data)
        user.set_password(form.password.data)
        user.save()
        flash('Congratulations, you are now a registered user!', 'alert-info')
        return redirect(prefix_url_for('login'))
    return render_template('auth/register.html', title='Register', form=form, prefix_url_for=prefix_url_for) 

@instance.route('/logout', strict_slashes=False)
def logout():
    logout_user()
    return redirect(prefix_url_for('index'))

"""
Authenticated Routes
"""
@instance.route('/dashboard', methods=['GET'], strict_slashes=False)
@login_required
def dashboard():
    jobs = Job.objects(user_id=current_user.id).order_by('-$natural').all()
    return render_template('dashboard.html', title='Dashboard', jobs=jobs, prefix_url_for=prefix_url_for)

@instance.route('/simulators/help', methods=['GET'], strict_slashes=False)
@login_required
def help():
    methods = [ 'IonTorrent', 'SOLiD', 'PacBio', '454', 'Illumina', 'Sanger', 'Nanopore' ]
    return render_template('help.html', title='Help', methods=methods, prefix_url_for=prefix_url_for)

@instance.route('/simulators/help/tree', methods=['GET'], strict_slashes=False)
@login_required
def help_tree():
    return render_template('tree.html', title='Help', prefix_url_for=prefix_url_for)

@instance.route('/simulators', methods=['GET'], strict_slashes=False)
@login_required
def simulators():
    return render_template('cards.html', title='Cards', simulators=SIMULATORS, prefix_url_for=prefix_url_for)

@instance.route('/download/<job_id>', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def download(job_id):
    client = arc.Client('newriver2.arc.vt.edu', arc.ARC_USER)
    local_path = os.path.join('/tmp', 'output.tar.gz')
    remote_path = os.path.join(arc.ARC_DIR, job_id, 'output.tar.gz')
    client.get_file(local_path, remote_path)
    client.close()
    return send_file(local_path)

@instance.route('/search', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def search():
    form = SearchForm()
    if form.validate_on_submit():
        requested_tags = {}
        keys = [ 'ref_db', 'genomics', 'tech', 'variants' ]
        for k in keys:
            requested_tags[k] = []
            for t in form.mapped_tags[k]:
                field_tuple = form.mapped_tags[k][t]
                field = field_tuple[0]
                if len(field_tuple) == 1 and field.data:
                    # list field
                    requested_tags[k].append(t)
                elif field.data:
                    # boolean field
                    kwargs = { k: field_tuple[1] }
                    requested_tags[k].append(Q(**kwargs))

        # http://docs.mongoengine.org/guide/querying.html#advanced-queries
        # Create the query object
        # Technology is a list query.
        if len(requested_tags['tech']) > 0:
            query = Q(tech__in=requested_tags['tech'])
        else:
            query = None

        # The other three keys are boolean queries.
        for key in [ 'ref_db', 'genomics', 'variants' ]:
            if len(requested_tags[key]) == 0:
                continue
            key_query = reduce((lambda q1, q2: q1 | q2), requested_tags[key])
            if query is None:
                query = key_query
            else:
                query = query & key_query

        if query is None:
            results = Job.objects()
        else:
            results = Job.objects(query)
        return render_template('search_results.html', title='Search Results', jobs=list(results), prefix_url_for=prefix_url_for)
    return render_template('search.html', title='Search', form=form, prefix_url_for=prefix_url_for)

"""
Simulator Routes
"""

def base_simulator_route(simulator, title, FormClass):
    form = FormClass()
    if form.validate_on_submit():
        create_and_start_job(simulator, form)
        return redirect(prefix_url_for('dashboard'))
    return render_template('simulators/{}.html'.format(simulator), title=title, form=form, prefix_url_for=prefix_url_for)

@instance.route('/simulators/454sim', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def sim_454():
    return base_simulator_route('454sim', '454Sim', Sim454Form)

@instance.route('/simulators/art_454', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def art_454():
    return base_simulator_route('art_454', 'ART 454', Art454Form)

@instance.route('/simulators/art_illumina', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def art_illumina():
    return base_simulator_route('art_illumina', 'ART Illumina', ArtIlluminaForm)

@instance.route('/simulators/art_solid', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def art_solid():
    return base_simulator_route('art_solid', 'ART SOLiD', ArtSolidForm)

@instance.route('/simulators/artificial_fastq_generator', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def artificial_fastq_generator():
    return base_simulator_route('artificialfastqgenerator', 'ArtificialFastqGenerator', ArtificialFastqGeneratorForm)

@instance.route('/simulators/bear_genomics_454', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def bear_genomics_454():
    return base_simulator_route('bear_genomics_454', 'BEAR Genomics 454', BearGenomics454Form)

@instance.route('/simulators/bear_genomics_illumina', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def bear_genomics_illumina():
    return base_simulator_route('bear_genomics_illumina', 'BEAR Genomics Illumina', BearGenomicsIlluminaForm)

@instance.route('/simulators/bear_genomics_iontorrent', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def bear_genomics_iontorrent():
    return base_simulator_route('bear_genomics_iontorrent', 'BEAR Genomics Iontorrent', BearGenomicsIontorrentForm)

@instance.route('/simulators/bear_metagenomics_454', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def bear_metagenomics_454():
    return base_simulator_route('bear_metagenomics_454', 'BEAR Metagenomics 454', BearMetagenomics454Form)

@instance.route('/simulators/bear_metagenomics_illumina', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def bear_metagenomics_illumina():
    return base_simulator_route('bear_metagenomics_illumina', 'BEAR Metagenomics Illumina', BearMetagenomicsIlluminaForm)

@instance.route('/simulators/bear_metagenomics_iontorrent', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def bear_metagenomics_iontorrent():
    return base_simulator_route('bear_metagenomics_iontorrent', 'BEAR Metagenomics Iontorrent', BearMetagenomicsIontorrentForm)

@instance.route('/simulators/curesim_illumina', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def curesim_illumina():
    return base_simulator_route('curesim_illumina', 'CuReSim Illumina', CuresimForm)

@instance.route('/simulators/curesim_solid', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def curesim_solid():
    return base_simulator_route('curesim_solid', 'CuReSim Solid', CuresimForm)

@instance.route('/simulators/curesim_iontorrent', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def curesim_iontorrent():
    return base_simulator_route('curesim_iontorrent', 'CuReSim Iontorrent', CuresimForm)

@instance.route('/simulators/curesim_454', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def curesim_454():
    return base_simulator_route('curesim_454', 'CuReSim 454', CuresimForm)

@instance.route('/simulators/dwgsim_illumina', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def dwgsim_illumina():
    return base_simulator_route('dwgsim_illumina', 'DWGSIM Illumina', DwgsimForm)

@instance.route('/simulators/dwgsim_solid', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def dwgsim_solid():
    return base_simulator_route('dwgsim_solid', 'DWGSIM Solid', DwgsimForm)

@instance.route('/simulators/dwgsim_iontorrent', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def dwgsim_iontorrent():
    return base_simulator_route('dwgsim_iontorrent', 'DWGSIM Iontorrent', DwgsimForm)

@instance.route('/simulators/eagle_454', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def eagle_454():
    return base_simulator_route('eagle_454', 'EAGLE 454', Eagle454Form)

@instance.route('/simulators/eagle_illumina', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def eagle_illumina():
    return base_simulator_route('eagle', 'EAGLE Illumina', EagleIlluminaForm)

@instance.route('/simulators/eagle_pacbio', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def eagle_pacbio():
    return base_simulator_route('eagle_pacbio', 'EAGLE PacBio', EaglePacbioForm)

@instance.route('/simulators/eagle_iontorrent', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def eagle_iontorrent():
    return base_simulator_route('eagle_iontorrent', 'EAGLE Iontorrent', EagleIontorrentForm)

@instance.route('/simulators/fastqsim_genomics_illumina', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def fastqsim_genomics_illumina():
    return base_simulator_route('fastqsim_genomics_illumina', 'FASTQSim Genomics Illumina', FastqsimGenomicsIlluminaForm)

@instance.route('/simulators/fastqsim_genomics_solid', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def fastqsim_genomics_solid():
    return base_simulator_route('fastqsim_genomics_solid', 'FASTQSim Genomics Solid', FastqsimGenomicsSolidForm)

@instance.route('/simulators/fastqsim_genomics_pacbio', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def fastqsim_genomics_pacbio():
    return base_simulator_route('fastqsim_genomics_pacbio', 'FASTQSim Genomics PacBio', FastqsimGenomicsPacBioForm)

@instance.route('/simulators/fastqsim_genomics_iontorrent', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def fastqsim_genomics_iontorrent():
    return base_simulator_route('fastqsim_genomics_iontorrent', 'FASTQSim Genomics IonTorrent', FastqsimGenomicsIontorrentForm)

@instance.route('/simulators/fastqsim_metagenomics_illumina', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def fastqsim_metagenomics_illumina():
    return base_simulator_route('fastqsim_metagenomics_illumina', 'FASTQSim Metagenomics Illumina', FastqsimMetagenomicsIlluminaForm)

@instance.route('/simulators/fastqsim_metagenomics_solid', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def fastqsim_metagenomics_solid():
    return base_simulator_route('fastqsim_metagenomics_solid', 'FASTQSim Metagenomics Solid', FastqsimMetagenomicsSolidForm)

@instance.route('/simulators/fastqsim_metagenomics_pacbio', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def fastqsim_metagenomics_pacbio():
    return base_simulator_route('fastqsim_metagenomics_pacbio', 'FASTQSim Metagenomics PacBio', FastqsimMetagenomicsPacBioForm)

@instance.route('/simulators/fastqsim_metagenomics_iontorrent', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def fastqsim_metagenomics_iontorrent():
    return base_simulator_route('fastqsim_metagenomics_iontorrent', 'FASTQSim Metagenomics Iontorrent', FastqsimMetagenomicsIontorrentForm)

@instance.route('/simulators/flowsim', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def flowsim():
    return base_simulator_route('flowsim', 'FlowSim', FlowsimForm)

@instance.route('/simulators/gemsim_genomics_illumina', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def gemsim_genomics_illumina():
    return base_simulator_route('gemsim_genomics_illumina', 'GemSim Genomics Illumina', GemsimGenomicsIlluminaForm)

@instance.route('/simulators/gemsim_genomics_454', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def gemsim_genomics_454():
    return base_simulator_route('gemsim_genomics_454', 'GemSim Genomics 454', GemsimGenomics454Form)

@instance.route('/simulators/gemsim_metagenomics_454', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def gemsim_metagenomics_454():
    return base_simulator_route('gemsim_metagenomics_454', 'GemSim Metagenomics 454', GemsimMetagenomics454Form)

@instance.route('/simulators/gemsim_metagenomics_illumina', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def gemsim_metagenomics_illumina():
    return base_simulator_route('gemsim_metagenomics_illumina', 'GemSim Metagenomics Illumina', GemsimMetagenomicsIlluminaForm)

@instance.route('/simulators/grinder_genomics_illumina', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def grinder_genomics_illumina():
    return base_simulator_route('grinder_genomics_illumina', 'Grinder Genomics Illumina', GrinderGenomicsIlluminaForm)

@instance.route('/simulators/grinder_genomics_454', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def grinder_genomics_454():
    return base_simulator_route('grinder_genomics_454', 'Grinder Genomics 454', GrinderGenomics454Form)

@instance.route('/simulators/grinder_genomics_sanger', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def grinder_genomics_sanger():
    return base_simulator_route('grinder_genomics_sanger', 'Grinder Genomics Sanger', GrinderGenomicsSangerForm)

@instance.route('/simulators/grinder_metagenomics_illumina', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def grinder_metagenomics_illumina():
    return base_simulator_route('grinder_metagenomics_illumina', 'Grinder Metagenomics Illumina', GrinderMetagenomicsIlluminaForm)
@instance.route('/simulators/grinder_metagenomics_454', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def grinder_metagenomics_454():
    return base_simulator_route('grinder_metagenomics_454', 'Grinder Metagenomics 454 ', GrinderMetagenomics454Form)
@instance.route('/simulators/grinder_metagenomics_sanger', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def grinder_metagenomics_sanger():
    return base_simulator_route('grinder_metagenomics_sanger', 'Grinder Metagenomics Sanger', GrinderMetagenomicsSangerForm)

@instance.route('/simulators/mason_genomics_454', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def mason_genomics_454():
    return base_simulator_route('mason_genomics_454', 'Mason Genomics 454', MasonSangerForm)

@instance.route('/simulators/mason_genomics_sanger', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def mason_genomics_sanger():
    return base_simulator_route('mason_genomics_sanger', 'Mason Genomics Sanger', MasonSangerForm)

@instance.route('/simulators/mason_genomics_illumina', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def mason_genomics_illumina():
    return base_simulator_route('mason_genomics_illumina', 'Mason Genomics Illumina', MasonSangerForm)

@instance.route('/simulators/mason_metagenomics_illumina', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def mason_metagenomics_illumina():
    return base_simulator_route('mason_metagenomics_illumina', 'Mason Metagenomics Illumina', MasonSangerForm)

@instance.route('/simulators/mason_metagenomics_454', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def mason_metagenomics_454():
    return base_simulator_route('mason_metagenomics_454', 'Mason Metagenomics 454', MasonSangerForm)

@instance.route('/simulators/mason_illumina', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def mason_illumina():
    return base_simulator_route('mason_illumina', 'Mason - Illumina', MasonIlluminaForm)

@instance.route('/simulators/metasim_genomics_illumina', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def metasim_genomics_illumina():
    return base_simulator_route('metasim_genomics_illumina', 'MetaSim Genomics Illumina', MetasimGenomicsIlluminaForm)

@instance.route('/simulators/metasim_genomics_454', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def metasim_genomics_454():
    return base_simulator_route('metasim_genomics_454', 'MetaSim Genomics 454', MetasimGenomics454Form)

@instance.route('/simulators/metasim_genomics_sanger', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def metasim_genomics_sanger():
    return base_simulator_route('metasim_genomics_sanger', 'MetaSim Genomics Sanger', MetasimGenomicsSangerForm)

@instance.route('/simulators/metasim_metagenomics_illumina', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def metasim_metagenomics_illumina():
    return base_simulator_route('metasim_metagenomics_illumina', 'MetaSim Metagenomics Illumina', MetasimMetagenomicsIlluminaForm)
@instance.route('/simulators/metasim_metagenomics_454', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def metasim_metagenomics_454():
    return base_simulator_route('metasim_metagenomics_454', 'MetaSim Metagenomics 454', MetasimMetagenomics454Form)
@instance.route('/simulators/metasim_metagenomics_sanger', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def metasim_metagenomics_sanger():
    return base_simulator_route('metasim_metagenomics_sanger', 'MetaSim Metagenomics Sanger', MetasimMetagenomicsSangerForm)

@instance.route('/simulators/nessm_illumina', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def nessm_illumina():
    return base_simulator_route('nessm_illumina', 'NeSSM Illumina', NessmIlluminaForm)

@instance.route('/simulators/nessm_454', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def nessm_454():
    return base_simulator_route('nessm_454', 'NeSSM 454', Nessm454Form)

@instance.route('/simulators/pbsim', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def pbsim():
    form = PbsimForm()
    if form.validate_on_submit():
        create_and_start_job('pbsim', form, form.fastq_file)
        return redirect(prefix_url_for('dashboard'))
    return render_template('simulators/{}.html'.format('pbsim'), title='Pbsim', form=form, prefix_url_for=prefix_url_for)

@instance.route('/simulators/readsim_nanopore', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def readsim_nanopore():
    return base_simulator_route('readsim_nanopore', 'ReadSim Nanopore', ReadsimNanoPoreForm)

@instance.route('/simulators/readsim_pacbio', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def readsim_pacbio():
    return base_simulator_route('readsim_pacbio', 'ReadSim PacBio', ReadsimPacBioForm)

@instance.route('/simulators/sinc', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def sinc():
    return base_simulator_route('sinc', 'SInC', SincForm)

@instance.route('/simulators/simseq', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def simseq():
    return base_simulator_route('simseq', 'SimSeq', SimseqForm)

@instance.route('/simulators/simhtsd_454', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def simhtsd_454():
    return base_simulator_route('simhtsd_454', 'Simhtsd 454', Simhtsd454Form)

@instance.route('/simulators/simhtsd_illumina', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def ssimhtsd_illumina():
    return base_simulator_route('simhtsd_illumina', 'Simhtsd Illumina', SimhtsdIlluminaForm)


@instance.route('/simulators/pirs_genomics_illumina', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def pirs_genomics_illumina():
    return base_simulator_route('pirs_genomics_illumina', 'pIRS Genomics Illumina', PirsForm)

@instance.route('/simulators/pirs_metagenomics_illumina', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def pirs_metagenomics_illumina():
    return base_simulator_route('pirs_metagenomics_illumina', 'pIRS Metagenomics Illumina', PirsForm)

@instance.route('/simulators/simngs', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def simngs():
    return base_simulator_route('simngs', 'simNGS', SimngsForm)

@instance.route('/simulators/wgsim_illumina', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def wgsim_illumina():
    return base_simulator_route('wgsim_illumina', 'wgsim Illumina', WgsimForm)

@instance.route('/simulators/wgsim_solid', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def wgsim_solid():
    return base_simulator_route('wgsim_solid', 'wgsim Solid', WgsimForm)

@instance.route('/simulators/xs_454', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def xs_454():
    return base_simulator_route('xs_454', 'xs 454', XsForm)

@instance.route('/simulators/xs_iontorrent', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def xs_iontorrent():
    return base_simulator_route('xs_iontorrent', 'xs Iontorrent', XsForm)

@instance.route('/simulators/xs_illumina', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def xs_illumina():
    return base_simulator_route('xs_illumina', 'xs Illumina', XsForm)

@instance.route('/simulators/xs_solid', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def xs_solid():
    return base_simulator_route('xs_solid', 'xs Solid', XsForm)

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
