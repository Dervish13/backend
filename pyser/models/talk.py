from peewee import BooleanField, DateTimeField, ForeignKeyField, TextField

from ..db import db
from .auth import User
from .date import datetime_format

Model = db.Model


class Talk(Model):
    description = TextField()
    end = DateTimeField(formats=[datetime_format], null=True)
    published = BooleanField(default=False)
    start = DateTimeField(formats=[datetime_format], null=True)
    text = TextField()
    title = TextField()
    user = ForeignKeyField(User, related_name='talks')
