from peewee import AutoField, CharField, DateTimeField, TextField
from app.models.base_model import BaseModel
from datetime import datetime

class User(BaseModel):
    # id = AutoField(primary_key=True)  # Clave primaria, ya viene de BaseModel
    first_name = CharField(max_length=50)  # Nombre
    last_name_1 = CharField(max_length=50)  # Primer apellido
    last_name_2 = CharField(max_length=50, null=True)  # Segundo apellido (opcional)
    email = CharField(null=False)  # No unico por si tenemos mas del mismo usuario
    phone = CharField(max_length=15, null=True)  # Teléfono (opcional)

    # Dirección
    address = TextField(null=True)  # Dirección completa
    city = CharField(max_length=100, null=True)  # Ciudad
    state = CharField(max_length=100, null=True)  # Estado/Provincia
    postal_code = CharField(max_length=20, null=True)  # Código postal
    country = CharField(max_length=100, null=True)  # País

    # Fechas de auditoría
    created_at = DateTimeField(default=datetime.now)  # Fecha de creación
    updated_at = DateTimeField(default=datetime.now)  # Fecha de última actualización