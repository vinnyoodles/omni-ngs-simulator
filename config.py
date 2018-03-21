import os

class Config(object):
    """
        List of configuration variables for the flask instances.
        Most, if not all, of the variables are defined as an environment variable.
        The definitions can be found in the docker-compose.yml file.
        The default values should not be used if Docker is running properly.
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret_key'
    MONGO_URL = os.environ.get('MONGO_URL') or 'mongodb://localhost:27017/simulator-db'
