from peewee import *
from database.database import BaseModel
from database.models.user import User


class UserBook(BaseModel):
    id = AutoField(),
    name = CharField(max_length=256, null=False),
    content = TextField(null=False),
    bookmark = IntegerField(null=True),

    user = ForeignKeyField(User, backref='user')
