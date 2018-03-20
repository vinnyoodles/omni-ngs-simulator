from flask import Flask
from flask_login import LoginManager
from config import Config
from mongoengine import connect

instance = Flask(__name__)
instance.config.from_object(Config)

login = LoginManager(instance)
login.login_view = 'auth.login'
login.login_message = 'Please log in to access this page.'

connect(host=instance.config['MONGO_URL'])

def create_app(config_class=Config):
    instance = Flask(__name__, static_url_path='/static')
    instance.config.from_object(config_class)

    login.init_app(instance)

    from app.home import bp as home_bp
    from app.auth import bp as auth_bp
    instance.register_blueprint(home_bp)
    instance.register_blueprint(auth_bp, url_prefix='/auth')

    return instance

from app import models
