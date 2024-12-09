from peewee import ForeignKeyField, CharField, DateField
from app.models.base_model import BaseModel
from app.models.user_model import User

class Course(BaseModel):
    user = ForeignKeyField(User, backref="courses", on_delete="CASCADE")
    title = CharField()
    institution = CharField(null=True)
    completion_date = DateField(null=True)
