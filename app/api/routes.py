from flask import jsonify, url_for, request
from flask_login import current_user
from app.api import bp
from app.models import User, Job
from app.tasks import start_job
import app.simulators as simulators


@bp.route('/users', methods=['GET'])
def get_users():
    return User.objects.all().to_json()

@bp.route('/spawn', methods=['POST'])
def spawn():
    task = start_job.apply_async(args=['bear.parametric_abundance', { 'output' : 'foo' }, 'test.out'])
    return jsonify({ 'task_id': task.id })

@bp.route('/jobs', methods=['POST'])
def create_job():
    if not current_user.is_authenticated:
        return jsonify(message='Must be logged in'), 401

    params = request.get_json()

    if not all(k in params for k in [ 'name', 'simulator', 'command' ]):
        return jsonify(message='Missing required arguments'), 400

    try:
        job_data = {
            'user_id'    : current_user.id,
            'name'       : params['name'],
            'status'     : 1,
            'simulator'  : int(params['simulator']),
            'command'    : params['command']
        }
    except ValueError:
        return jsonify(message='Simulator parameter must be an integer'), 400
    except Exception as e:
        return jsonify(message=str(e), parameters=params), 500

    job = Job(**job_data)
    job.save()
    return jsonify(job.to_json())

@bp.route('/jobs', methods=['GET'])
def get_jobs():
    return Job.objects.all().to_json()

@bp.route('/simulators', methods=['GET'])
def get_simulators():
    return jsonify(simulators.to_json())
