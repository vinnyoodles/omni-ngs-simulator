from flask import Flask
from flask_login import LoginManager
from config import Config
from mongoengine import connect
from celery import Celery

instance = Flask(__name__, static_url_path='/static')
instance.config.from_object(Config)

login = LoginManager(instance)
login.login_message = 'Please log in to access this page.'
login.login_view = 'login'

celery = Celery(instance.name, broker=Config.CELERY_BROKER_URL)
celery.conf.update(instance.config)

connect(host=instance.config['MONGO_URL'])

from app import models, routes, tasks