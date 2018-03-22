from flask import render_template
from app.home import bp
from app.models import User
from app.simulators import SIMULATORS


@bp.route('/')
def index():
    return render_template('index.html', title='Home', transparent_nav=True)

@bp.route('/simulators')
def simulators():
    return render_template('cards.html', title='Cards', simulators=SIMULATORS)
