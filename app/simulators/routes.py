from flask import render_template, flash, redirect, jsonify, url_for
from app.simulators import bp

@bp.route('/bear/parametric_abundance', methods=['GET'])
def bear_parametric_abundance():
    return render_template('simulators/bear_parametric_abundance.html', title='Bear')