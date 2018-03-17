from flask import render_template
from app import instance

@instance.route('/')
@instance.route('/index')
def index():
    user = { 'username': 'vinnyoodles' }
    return render_template('index.html', title='Home', user=user)