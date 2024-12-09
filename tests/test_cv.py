import os
import unittest
from peewee import SqliteDatabase
from app.models.cv_model import CVModel
from app.models.user_model import User
from app.services.cv_service import CVService

class TestCVModelAndService(unittest.TestCase):
    """Pruebas unitarias para el modelo CVModel y el servicio CVService."""

    @classmethod
    def setUpClass(cls):
        """Configura una base de datos en memoria para las pruebas."""
        cls.test_db = SqliteDatabase(':memory:')
        cls.test_db.bind([User, CVModel], bind_refs=False, bind_backrefs=False)
        cls.test_db.connect()
        cls.test_db.create_tables([User, CVModel])

    @classmethod
    def tearDownClass(cls):
        """Desconecta y elimina la base de datos en memoria."""
        cls.test_db.drop_tables([User, CVModel])
        cls.test_db.close()

    def setUp(self):
        """Configura datos iniciales para las pruebas."""
        self.user = User.create(
            first_name="John",
            last_name_1="Doe",
            last_name_2="Smith",
            email="johndoe@example.com"
        )

    def tearDown(self):
        """Limpia los datos entre pruebas."""
        CVModel.delete().execute()
        User.delete().execute()

    def test_create_cv(self):
        """Prueba la creación de un CV mediante CVService."""
        personal_info = {
            "name": "John Doe",
            "address": "123 Main Street",
            "phone": "123-456-7890",
            "email": "johndoe@example.com"
        }
        professional_summary = "Software engineer with 5 years of experience."
        work_experience = [
            {
                "job_title": "Developer",
                "company": "TechCorp",
                "duration": "2018-2023",
                "responsibilities": ["Developed applications", "Led team projects"]
            }
        ]
        education = [{"degree": "B.Sc. Computer Science", "institution": "Tech University", "year": "2018"}]
        skills = ["Python", "SQL", "JavaScript"]
        certifications = ["AWS Certified Developer"]
        projects = [{"title": "Project A", "description": "A web-based application"}]

        cv = CVService.create_cv(
            user_id=self.user.id,
            personal_info=personal_info,
            professional_summary=professional_summary,
            work_experience=work_experience,
            education=education,
            skills=skills,
            certifications=certifications,
            projects=projects
        )

        self.assertIsNotNone(cv)
        self.assertEqual(cv.user_id.id, self.user.id)
        self.assertEqual(cv.personal_info['name'], "John Doe")

    def test_generate_pdf(self):
        """Prueba la generación de un CV en formato PDF."""
        personal_info = {
            "name": "John Doe",
            "address": "123 Main Street",
            "phone": "123-456-7890",
            "email": "johndoe@example.com"
        }
        cv = CVModel.create(
            user_id=self.user.id,
            personal_info=personal_info,
            professional_summary="Summary",
            work_experience=[],
            education=[],
            skills=[],
            certifications=[],
            projects=[]
        )

        file_path = "test_cv.pdf"
        try:
            CVService.generate_pdf(cv.id, file_path)
            self.assertTrue(os.path.exists(file_path))
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_generate_word(self):
        """Prueba la generación de un CV en formato Word (DOCX)."""
        personal_info = {
            "name": "John Doe",
            "address": "123 Main Street",
            "phone": "123-456-7890",
            "email": "johndoe@example.com"
        }
        cv = CVModel.create(
            user_id=self.user.id,
            personal_info=personal_info,
            professional_summary="Summary",
            work_experience=[],
            education=[],
            skills=[],
            certifications=[],
            projects=[]
        )

        file_path = "test_cv.docx"
        try:
            CVService.generate_word(cv.id, file_path)
            self.assertTrue(os.path.exists(file_path))
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_generate_html(self):
        """Prueba la generación de un CV en formato HTML."""
        personal_info = {
            "name": "John Doe",
            "address": "123 Main Street",
            "phone": "123-456-7890",
            "email": "johndoe@example.com"
        }
        cv = CVModel.create(
            user_id=self.user.id,
            personal_info=personal_info,
            professional_summary="Summary",
            work_experience=[],
            education=[],
            skills=[],
            certifications=[],
            projects=[]
        )

        file_path = "test_cv.html"
        try:
            CVService.generate_html(cv.id, file_path)
            self.assertTrue(os.path.exists(file_path))
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

if __name__ == "__main__":
    unittest.main()
