import peewee
from peewee import *
from app import db


# class BaseModel(Model):
#     class Meta:
#         database = db
#         table_name = 'sc_user'


class User(Model):
    id = PrimaryKeyField(null=False)
    name = CharField(max_length=35)

    def dict(self):
        return {'id': self.id, 'name': self.name}

    class Meta:
        database = db
        table_name = 'sc_user'
