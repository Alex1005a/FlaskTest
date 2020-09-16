from flask_login import UserMixin
from flask_mongoengine import MongoEngine

db = MongoEngine()

class User(db.Document, UserMixin):
    name = db.StringField(max_length=20, required=True, unique=True)
    password = db.StringField(required=True)

    def get_id(self):
        return str(self.pk)

class Task(db.Document):
    userId = db.StringField(max_length=25, required=True)
    title = db.StringField(max_length=25, required=True)
    description = db.StringField(max_length=100, required=True)
    performed = db.BooleanField(default=False, required=True)
    def get_id(self):
        return str(self.pk)