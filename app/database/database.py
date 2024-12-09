from peewee import SqliteDatabase
import os

# Peewee incluye automaticamente una PK id, pero lo haremos explicitamente

DB_PATH = os.getenv("DB_FULL_PATH")
db = SqliteDatabase(DB_PATH, pragmas={"foreign_keys": 1})  # Activar claves foráneas


# Conexión para todos los modelos
def init_db():
    from app.models import (
        User,
        SocialLink,
        Skill,
        Job,
        Course,
        Project,
        Education,
        Template,
    )
    db.connect()
    # db.create_tables([User, SocialLink, Skill, Job, Course, Project, Education, Template])
   
   # Verificar si las tablas ya existen
    existing_tables = db.get_tables()

    # Filtrar las tablas que faltan
    # En teoria peewee no sobreescribe algo que ya existe, pero por si acaso.
    tables_to_create = [
        model for model in [User, SocialLink, Skill, Job, Course, Project, Education, Template]
        if model._meta.table_name not in existing_tables
    ]

    if tables_to_create:
        db.create_tables(tables_to_create)