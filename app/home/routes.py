from flask import render_template
from flask_login import current_user, login_required
from app.home import bp
from app.models import User

@bp.route('/')
def index():
    return render_template('index.html', title='Home', transparent_nav=True)

@bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', title='Dashboard')