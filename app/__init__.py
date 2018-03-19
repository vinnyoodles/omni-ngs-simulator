from flask import Flask
from flask_login import LoginManager
from config import Config
from mongoengine import connect

instance = Flask(__name__)
instance.config.from_object(Config)

login = LoginManager(instance)
login.login_view = 'login'

connect(host=instance.config['MONGO_URL'])

# Import routes at the bottom due to circular imports
from app import routes