import os
from flask import render_template, flash, redirect, jsonify, url_for
from flask_login import current_user, login_required
from app.simulators import bp, SIMULATORS, parse_commandline
from app.auth.forms import BearParametricAbundanceForm
from app.models import Job
from app.tasks import start_job

def create_and_start_job(sim_id, name, command_args, file):
    data = {
        'status'    : 'pending',
        'simulator' : sim_id,
        'user_id'   : current_user.id,
        'name'      : name
    }
    job = Job(**data)

    if name is None:
        job.name = name = str(job.id)

    job.save()

    # The path where all output files are written to is the project's directory.
    # TODO: for dev purposes, this is okay (change for production)
    input_filename = os.path.join('/app', '{}_{}.in'.format(sim_id, job.id))
    output_filename = os.path.join('/app', '{}_{}.out'.format(sim_id, job.id))
    file.save(input_filename)

    command_args['input'] = input_filename
    command_args['output'] = output_filename
    command_arr = parse_commandline(SIMULATORS[sim_id], command_args)
    job.command = ' '.join(command_arr)
    job.save()
    start_job.apply_async(args=[sim_id, command_args, output_filename])
    return (job, command_arr)

@bp.route('/')
@login_required
def simulators():
    return render_template('cards.html', title='Cards', simulators=SIMULATORS)

@bp.route('/bear/parametric_abundance', methods=['GET', 'POST'])
@login_required
def bear_parametric_abundance():
    form = BearParametricAbundanceForm()
    if form.validate_on_submit():
        create_and_start_job('bear.parametric_abundance', form.name.data, { 'complexity' : form.complexity.data }, form.file.data)
        return redirect(url_for('home.dashboard'))

    return render_template('simulators/bear_parametric_abundance.html', title='Bear', form=form)