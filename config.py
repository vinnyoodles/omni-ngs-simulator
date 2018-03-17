import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret_key'
    MONGO_URL = os.environ.get('MONGO_URL') or 'mongodb://localhost:27017/simulator-db'
