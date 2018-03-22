from flask import render_template, flash, redirect, jsonify, url_for
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename
from app.simulators import bp, SIMULATORS
from app.auth.forms import BearParametricAbundanceForm

@bp.route('/')
@login_required
def simulators():
    return render_template('cards.html', title='Cards', simulators=SIMULATORS)

@bp.route('/bear/parametric_abundance', methods=['GET', 'POST'])
@login_required
def bear_parametric_abundance():
    form = BearParametricAbundanceForm()
    if form.validate_on_submit():
        # TODO: https://flask-wtf.readthedocs.io/en/stable/form.html#module-flask_wtf.file
        return redirect(url_for('home.index'))
    return render_template('simulators/bear_parametric_abundance.html', title='Bear', form=form)