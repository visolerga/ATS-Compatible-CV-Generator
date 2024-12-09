import unittest
from peewee import SqliteDatabase
from app.database.database import init_db
from app.models.user_model import User
from app.models.social_link_model import SocialLink
from app.models.skill_model import Skill
from app.models.job_model import Job
from app.models.course_model import Course
from app.models.project_model import Project
from app.models.education_model import Education
from app.models.template_model import Template

# Configura la base de datos para pruebas
test_db = SqliteDatabase(':memory:')  # Usar una base de datos en memoria para pruebas

class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Conectar a la base de datos de prueba y crear tablas
        cls.db = test_db
        cls.db.connect()
        init_db()  # Inicializa las tablas de modelos
        cls.db.create_tables([User, SocialLink, Skill, Job, Course, Project, Education, Template])

    @classmethod
    def tearDownClass(cls):
        # Cerrar la conexión y eliminar las tablas después de las pruebas
        cls.db.drop_tables([User, SocialLink, Skill, Job, Course, Project, Education, Template])
        cls.db.close()

class TestUserModel(BaseTestCase):
    def test_create_user(self):
        user = User.create(
            first_name='John',
            last_name_1='Doe',
            last_name_2='Smith',
            email='john.doe@example.com',
            phone='1234567890',
            address='123 Main St',
            city='Anytown',
            state='Anystate',
            postal_code='12345',
            country='Country'
        )
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.email, 'john.doe@example.com')

# Puedes agregar más clases de prueba para otros modelos aquí

class TestSocialLinkModel(BaseTestCase):
    def test_create_social_link(self):
        user = User.create(
            first_name='Jane',
            last_name_1='Doe',
            email='jane.doe@example.com'
        )
        social_link = SocialLink.create(
            user_id=user.id,
            platform='LinkedIn',
            url='https://www.linkedin.com/in/janedoe/'
        )
        self.assertEqual(social_link.platform, 'LinkedIn')
        self.assertEqual(social_link.url, 'https://www.linkedin.com/in/janedoe/')

class TestSkillModel(BaseTestCase):
    def test_create_skill(self):
        user = User.create(
            first_name='Alice',
            last_name_1='Smith',
            email='alice.smith@example.com'
        )
        skill = Skill.create(
            name='Python',
            source_type='course',
            user_id=user.id
        )
        self.assertEqual(skill.name, 'Python')
        self.assertEqual(skill.source_type, 'course')

class TestJobModel(BaseTestCase):
    def test_create_job(self):
        user = User.create(
            first_name='Bob',
            last_name_1='Brown',
            email='bob.brown@example.com'
        )
        job = Job.create(
            user_id=user.id,
            company='Tech Corp',
            role='Developer',
            start_date='2022-01-01',
            end_date='2023-01-01',
            description='Developing software applications.'
        )
        self.assertEqual(job.company, 'Tech Corp')
        self.assertEqual(job.role, 'Developer')

class TestCourseModel(BaseTestCase):
    def test_create_course(self):
        user = User.create(
            first_name='Eve',
            last_name_1='Johnson',
            email='eve.johnson@example.com'
        )
        course = Course.create(
            user_id=user.id,
            title='Python Programming',
            institution='Online University',
            completion_date='2023-06-30'
        )
        self.assertEqual(course.title, 'Python Programming')
        self.assertEqual(course.institution, 'Online University')

class TestProjectModel(BaseTestCase):
    def test_create_project(self):
        user = User.create(
            first_name='Charlie',
            last_name_1='Davis',
            email='charlie.davis@example.com'
        )
        project = Project.create(
            user_id=user.id,
            title='Personal Website',
            description='Created a personal portfolio website.',
            url='https://charliedavis.com'
        )
        self.assertEqual(project.title, 'Personal Website')
        self.assertEqual(project.url, 'https://charliedavis.com')

class TestEducationModel(BaseTestCase):
    def test_create_education(self):
        user = User.create(
            first_name='Grace',
            last_name_1='Lee',
            email='grace.lee@example.com'
        )
        education = Education.create(
            user_id=user.id,
            degree='Bachelor of Science',
            institution='University of Example',
            start_date='2018-09-01',
            end_date='2022-06-15'
        )
        self.assertEqual(education.degree, 'Bachelor of Science')
        self.assertEqual(education.institution, 'University of Example')

class TestTemplateModel(BaseTestCase):
    def test_create_template(self):
        user = User.create(
            first_name='Dana',
            last_name_1='Miller',
            email='dana.miller@example.com'
        )
        template = Template.create(
            user_id=user.id,
            name='Basic CV Template',
            font='Arial',
            font_size=12,
            line_spacing=1.5
        )
        self.assertEqual(template.name, 'Basic CV Template')
        self.assertEqual(template.font, 'Arial')

if __name__ == '__main__':
    unittest.main()
