import datetime
from peewee import *
from database.database import peewee_db


class User(Model):
    class Meta:
        database = peewee_db

    ref_key = UUIDField()
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now, constraints=[SQL('ON UPDATE CURRENT_TIMESTAMP')])

    username = CharField()
    password = CharField()
