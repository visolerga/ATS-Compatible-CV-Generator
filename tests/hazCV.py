import os
from peewee import SqliteDatabase
from app.models.cv_model import CVModel
from app.models.user_model import User
from app.services.cv_service import CVService


# Configuración de la base de datos en memoria para pruebas
db = SqliteDatabase(':memory:')
db.bind([User, CVModel], bind_refs=False, bind_backrefs=False)
db.connect()
db.create_tables([User, CVModel])

try:
    # Crear un usuario de prueba
    user = User.create(
        first_name="Jane",
        last_name_1="Doe",
        last_name_2="Smith",
        email="janedoe@example.com"
    )

    # Crear un CV de prueba
    personal_info = {
        "name": "Jane Doe",
        "address": "456 Elm Street",
        "phone": "987-654-3210",
        "email": "janedoe@example.com"
    }
    professional_summary = "Experienced graphic designer with expertise in visual storytelling."
    work_experience = [
        {
            "job_title": "Graphic Designer",
            "company": "Creative Studio",
            "duration": "2015-2023",
            "responsibilities": [
                "Created brand identities",
                "Designed marketing materials",
                "Led creative projects"
            ]
        }
    ]
    education = [
        {"degree": "B.A. Graphic Design", "institution": "Art University", "year": "2015"}
    ]
    skills = ["Adobe Photoshop", "Illustrator", "InDesign"]
    certifications = ["Certified Adobe Expert"]
    projects = [
        {"title": "Brand Redesign", "description": "Redesigned branding for a major retailer."}
    ]

    cv = CVModel.create(
        user_id=user.id,
        personal_info=personal_info,
        professional_summary=professional_summary,
        work_experience=work_experience,
        education=education,
        skills=skills,
        certifications=certifications,
        projects=projects
    )

    # Ruta para guardar el archivo
    output_file = "test_cv.docx"

    # Generar el archivo Word
    CVService.generate_word(cv.id, output_file)

    # Verificar si el archivo se ha creado
    if os.path.exists(output_file):
        print(f"El archivo {output_file} se ha generado correctamente.")
    else:
        print(f"Error: No se pudo generar el archivo {output_file}.")

finally:
    # Limpieza de base de datos
    db.drop_tables([User, CVModel])
    db.close()
