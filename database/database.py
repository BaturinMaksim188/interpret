import datetime

from peewee import *

peewee_db = SqliteDatabase('database.db')


class BaseModel(Model):
    class Meta:
        database = peewee_db


class UserBook(BaseModel):
    id = AutoField()
    ref_key = UUIDField()
    name = CharField(max_length=256, null=False)
    author = CharField(max_length=256, null=True)
    content = TextField(null=False)
    bookmark = IntegerField(null=True)
    format = CharField(max_length=256, null=True)


class User(BaseModel):
    ref_key = UUIDField()
    username = CharField()
    password = CharField()


peewee_db.connect()
peewee_db.create_tables([User, UserBook])
peewee_db.close()

print('Succes')
