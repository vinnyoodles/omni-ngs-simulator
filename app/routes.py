from flask import render_template, flash, redirect, jsonify, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from app.simulators import SIMULATORS, sim_json
from app.forms import LoginForm, RegistrationForm, BearParametricAbundanceForm
from app.tasks import create_and_start_job
from app.models import User
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
            flash('Invalid email or password')
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
        flash('Congratulations, you are now a registered user!')
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
    return render_template('dashboard.html', title='Dashboard')

@instance.route('/simulators', methods=['GET'], strict_slashes=False)
@login_required
def simulators():
    return render_template('cards.html', title='Cards', simulators=SIMULATORS)


@instance.route('/simulators/bear/parametric_abundance', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def bear_parametric_abundance():
    form = BearParametricAbundanceForm()
    if form.validate_on_submit():
        create_and_start_job('bear.parametric_abundance', form.name.data, { 'complexity' : form.complexity.data }, form.file.data)
        return redirect(url_for('dashboard'))

    return render_template('simulators/bear_parametric_abundance.html', title='Bear', form=form)

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