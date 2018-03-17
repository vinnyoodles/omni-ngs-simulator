from flask import render_template, flash, redirect
from app import instance
from app.forms import LoginForm

@instance.route('/')
@instance.route('/index')
def index():
    user = { 'username': 'vinnyoodles' }
    return render_template('index.html', title='Home', user=user)

@instance.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign -In', form=form)