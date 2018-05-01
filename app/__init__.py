from flask import Flask
from flask_login import LoginManager
from config import Config
from mongoengine import connect
from celery import Celery
from werkzeug.routing import Rule

ROUTE_PREFIX = '/prefix'

instance = Flask(__name__, static_url_path=ROUTE_PREFIX + '/static')
instance.config.from_object(Config)
instance.url_rule_class = lambda path, **options: Rule(ROUTE_PREFIX + path, **options)


login = LoginManager(instance)
login.login_message = 'Please log in to access this page.'
login.login_view = 'login'

celery = Celery(instance.name, broker=Config.CELERY_BROKER_URL)
celery.conf.update(instance.config)

connect(host=instance.config['MONGO_URL'])

from app import models, routes, tasks