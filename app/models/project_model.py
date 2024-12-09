from peewee import ForeignKeyField, CharField, TextField
from app.models.base_model import BaseModel
from app.models.user_model import User

class Project(BaseModel):
    user = ForeignKeyField(User, backref="projects", on_delete="CASCADE")
    title = CharField()
    description = TextField(null=True)
    url = CharField(null=True)
