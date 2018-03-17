from flask import Flask

instance = Flask(__name__)

# Import routes at the bottom due to circular imports
from app import routes