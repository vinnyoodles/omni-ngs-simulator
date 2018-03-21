from flask import render_template
from app.home import bp
from app.models import User

@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html', title='Home', transparent_nav=True)
