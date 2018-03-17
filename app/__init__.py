from flask import Flask
from config import Config
from mongoengine import connect

instance = Flask(__name__)
instance.config.from_object(Config)

connect(host=instance.config['MONGO_URL'])

# Import routes at the bottom due to circular imports
from app import routes