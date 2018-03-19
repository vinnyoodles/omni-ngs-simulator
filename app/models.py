from werkzeug.security import generate_password_hash, check_password_hash
from mongoengine import *
from flask_login import UserMixin
from app import login

class User(UserMixin, Document):
    email = StringField(required=True)
    password_hash = StringField(required=True)
    institution = StringField(required=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(user_id):
    return User.objects(id=user_id).first()