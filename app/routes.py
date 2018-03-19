from flask import render_template, flash, redirect, jsonify, url_for
from flask_login import current_user, login_user, logout_user
from app import instance
from app.forms import LoginForm
from models import User

@instance.route('/')
@instance.route('/index')
def index():
    return render_template('index.html', title='Home')

@instance.route('/login', methods=['GET', 'POST'])
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
        return redirect('/index')
    return render_template('login.html', title='Login', form=form)

@instance.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@instance.route('/api/users', methods=['GET'])
def get_users():
    return User.objects.all().to_json()