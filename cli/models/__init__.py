from peewee import *
import datetime

db = MySQLDatabase("guest", host="127.0.0.1", port=3306, user="root", passwd="123456")
db.connect()


class BaseModel(Model):

    class Meta:
        database = db


class User(BaseModel):
    username = CharField(unique=True)

class Member(BaseModel):
    user = ForeignKeyField(User, related_name='tweets')
    message = TextField()
    created_date = DateTimeField(default=datetime.datetime.now)
    is_published = BooleanField(default=True)


class Group(BaseModel):
    user = ForeignKeyField(User, related_name='tweets')
    message = TextField()
    created_date = DateTimeField(default=datetime.datetime.now)
    is_published = BooleanField(default=True)
