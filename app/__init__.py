from flask import Flask
from flask_login import LoginManager
from config import Config
from mongoengine import connect
from celery import Celery

login = LoginManager()
login.login_view = 'auth.login'

celery = Celery(__name__, broker=Config.CELERY_BROKER_URL)

def create_app(config_class=Config):
    """
        The flask instance is setup and organized using the application factory pattern.
        This makes it configurable for other uses such as testing.
    """
    instance = Flask(__name__, static_url_path='/static')
    instance.config.from_object(config_class)

    login.login_message = 'Please log in to access this page.'
    login.init_app(instance)

    connect(host=instance.config['MONGO_URL'])

    celery.conf.update(instance.config)

    from app.home import bp as home_bp
    from app.auth import bp as auth_bp
    from app.api import bp as api_bp
    instance.register_blueprint(home_bp)
    instance.register_blueprint(auth_bp, url_prefix='/auth')
    instance.register_blueprint(api_bp, url_prefix='/api/v1.0')

    return instance

from app import models
