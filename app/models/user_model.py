from peewee import CharField, DateTimeField
from app.models.base_model import BaseModel
from datetime import datetime

class User(BaseModel):
    name = CharField()
    email = CharField(unique=True)
    phone = CharField(null=True)
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)
