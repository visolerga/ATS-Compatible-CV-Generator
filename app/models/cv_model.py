from peewee import Model, CharField, TextField, DateField, ForeignKeyField, JSONField
from app.models.base_model import BaseModel
from app.models.user_model import User

class CVModel(BaseModel):
    """Modelo para almacenar información relacionada con el CV."""
    user_id = ForeignKeyField(User, backref='cvs', on_delete='CASCADE')
    
    # Usamos JSONField para almacenar datos estructurados
    personal_info = JSONField()  # { "name": "Nombre", "address": "Dirección", "phone": "Teléfono", "email": "Correo electrónico" }
    professional_summary = TextField()  # Resumen profesional
    work_experience = JSONField()  # [{ "job_title": "Título", "company": "Empresa", "duration": "Duración", "responsibilities": ["Responsabilidad 1", "Responsabilidad 2"] }]
    education = JSONField()  # [{ "degree": "Grado", "institution": "Institución", "year": "Año" }]
    skills = JSONField()  # ["Habilidad 1", "Habilidad 2"]
    certifications = JSONField()  # [{ "certification": "Certificación", "issuer": "Emisor", "year": "Año" }]
    projects = JSONField()  # [{ "project_name": "Nombre del Proyecto", "description": "Descripción" }]
    references = JSONField(null=True)  # [{ "name": "Nombre", "contact_info": "Información de contacto" }]
