# Metaclase para la definicion de los modelos
# Peewee incluye automaticamente una pk id, pero por si acaso lo incluimos
# Como las otras clases lo heredan, no hara falta redefinirlo en cada una
from peewee import Model, AutoField
from app.database.database import db

class BaseModel(Model):
    # Clave primaria automática
    id = AutoField(primary_key=True) 
    class Meta:
        database = db
