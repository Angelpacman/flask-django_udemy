import datetime

from peewee import *

DATABASE = SqliteDatabase('social.db')

class User(usernixin,model):
    username    = Charfield(unique=True)
    email       = Charfield(unique=True)
    password    = Charfield(max_length = 120)
    joined_at   = DateTimeField(default = datetime.datetime.now)

    class Meta:
        database = DATABASE
        order_by = ('-joined_at')
