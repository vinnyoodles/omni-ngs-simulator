from flask import Flask
from config import Config

instance = Flask(__name__)
instance.config.from_object(Config)

# Import routes at the bottom due to circular imports
from app import routes