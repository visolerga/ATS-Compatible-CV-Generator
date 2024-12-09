from peewee import ForeignKeyField, CharField
from app.models.base_model import BaseModel
from app.models.user_model import User

class SocialLink(BaseModel):
    user = ForeignKeyField(User, backref="social_links", on_delete="CASCADE")
    platform = CharField()
    url = CharField()
