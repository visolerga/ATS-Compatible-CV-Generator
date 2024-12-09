from peewee import ForeignKeyField, TextField, CharField
from app.models.base_model import BaseModel
from app.models.user_model import User

class Template(BaseModel):
    user = ForeignKeyField(User, backref="templates", on_delete="CASCADE")
    name = CharField()
    content = TextField()  # JSON o texto con configuración y datos
