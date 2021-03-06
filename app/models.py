from werkzeug.security import generate_password_hash, check_password_hash
from mongoengine import *
from flask_login import UserMixin
from app import login

class User(UserMixin, Document):
    email              = StringField(required=True, unique=True)
    password_hash      = StringField(required=True)
    institution        = StringField(required=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Job(Document):
    user_id            = ObjectIdField(required=True)
    privacy            = StringField(required=True)
    name               = StringField()
    simulator          = StringField(required=True)
    status             = StringField(required=True)
    attrs              = DictField(required=True)
    command            = StringField()
    err                = StringField()
    ref_db             = BooleanField(required=True)
    variants           = BooleanField(required=True)
    genomics           = BooleanField(required=True)
    tech               = ListField(required=True)

@login.user_loader
def load_user(user_id):
    """
        Helper function for the flask login module.
        This is the authentication logic to verify if a user exists in the database or not.
    """
    return User.objects(id=user_id).first()