from mongoengine import *

class User(Document):
    email = StringField(required=True)
    password_hash = StringField(required=True)
    institution = StringField(required=True)