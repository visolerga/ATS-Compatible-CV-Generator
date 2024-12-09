from peewee import ForeignKeyField, CharField, TextField, DateField
from app.models.base_model import BaseModel
from app.models.user_model import User

class Job(BaseModel):
    user = ForeignKeyField(User, backref="jobs", on_delete="CASCADE")
    company = CharField()
    role = CharField()
    start_date = DateField()
    end_date = DateField(null=True)
    description = TextField(null=True)
