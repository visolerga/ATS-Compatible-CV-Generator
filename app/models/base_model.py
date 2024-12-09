from peewee import ForeignKeyField, CharField, DateField
from app.models.base_model import BaseModel
from app.models.user_model import User

class Education(BaseModel):
    user = ForeignKeyField(User, backref="education", on_delete="CASCADE")
    degree = CharField()
    institution = CharField()
    start_date = DateField()
    end_date = DateField(null=True)
from peewee import Model
from app.database.database import db

class BaseModel(Model):
    class Meta:
        database = db
