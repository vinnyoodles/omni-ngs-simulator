import os
from flask import Flask
from flask_login import LoginManager
from config import Config
from mongoengine import connect
from celery import Celery
from werkzeug.routing import Rule

PROD_ENV = os.environ.get('PROD_ENV') == '1'

ROUTE_PREFIX = ''
if PROD_ENV:
    ROUTE_PREFIX = '/omningssimulator'

instance = Flask(__name__, static_url_path='/static')
instance.config.from_object(Config)
instance.url_rule_class = lambda path, **options: Rule(ROUTE_PREFIX + path, **options)

login = LoginManager(instance)
login.login_message = 'Please log in to access this page.'
login.login_view = 'login'

celery = Celery(instance.name, broker=Config.CELERY_BROKER_URL)
celery.conf.update(instance.config)

connect(host=instance.config['MONGO_URL'])

from app import models, routes, tasks
