from flask import render_template, flash, redirect, jsonify, url_for, request
from flask_login import current_user, login_user, logout_user
from werkzeug.urls import url_parse
from app.auth.forms import LoginForm, RegistrationForm
from app.auth import bp
from app.models import User

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home.index'))
    form = LoginForm()

    if form.validate_on_submit():
        user = User.objects(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid email or password')
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)

        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('auth/login.html', title='Login', form=form)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, institution=form.institution.data)
        user.set_password(form.password.data)
        user.save()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', title='Register', form=form) 

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home.index'))
