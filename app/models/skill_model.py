from peewee import ForeignKeyField, CharField
from app.models.base_model import BaseModel
from app.models.user_model import User

class Skill(BaseModel):
    user = ForeignKeyField(User, backref="skills", on_delete="CASCADE")
    name = CharField()
    source_type = CharField(choices=[("job", "Job"), ("course", "Course")])
    source_id = CharField(null=True)
