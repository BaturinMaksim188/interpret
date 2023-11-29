import datetime

from peewee import *

peewee_db = SqliteDatabase('database.db')


class BaseModel(Model):
    class Meta:
        database = peewee_db


class UserBook(BaseModel):
    id = AutoField()
    name = CharField(max_length=256, null=False)
    author = CharField(max_length=256, null=True)
    content = TextField(null=False)
    bookmark = IntegerField(null=True)


class User(Model):
    class Meta:
        database = peewee_db

    ref_key = UUIDField()
    username = CharField()
    password = CharField()


peewee_db.connect()
peewee_db.create_tables([User, UserBook])
peewee_db.close()

print('Succes')
