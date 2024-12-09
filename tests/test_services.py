# app/tests/test_services.py

import unittest
from app.services.user_service import UserService
from app.services.course_service import CourseService
from app.services.education_service import EducationService
from app.services.job_service import JobService
from app.services.project_service import ProjectService
from app.services.skill_service import SkillService
from app.services.social_link_service import SocialLinkService
from app.services.template_service import TemplateService
from app.models import User, Course, Education, Job, Project, Skill, SocialLink, Template
from peewee import SqliteDatabase

class TestServices(unittest.TestCase):
    """Clase de pruebas para los servicios de la aplicación.
    
    Esta clase contiene pruebas para cada uno de los servicios que interactúan 
    con la base de datos, asegurando que las operaciones CRUD (Crear, Leer, 
    Actualizar, Eliminar) funcionen correctamente.
    """

    @classmethod
    def setUpClass(cls):
        """Configura el entorno de prueba antes de ejecutar las pruebas."""
        cls.database = SqliteDatabase(':memory:')
        cls.database.connect()
        cls.database.create_tables([User, Course, Education, Job, Project, Skill, SocialLink, Template])

    @classmethod
    def tearDownClass(cls):
        """Limpia el entorno de prueba después de ejecutar las pruebas."""
        cls.database.close()

    def test_create_user(self):
        """Prueba la creación de un nuevo usuario."""
        user = UserService.create_user(
            first_name='John',
            last_name_1='Doe',
            last_name_2='Smith',
            email='john.doe@example.com',
            phone='1234567890'
        )
        self.assertIsNotNone(user.id)  # Verifica que se haya asignado un ID
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.email, 'john.doe@example.com')

    def test_get_user_by_id(self):
        """Prueba la obtención de un usuario por su ID."""
        user = UserService.create_user(
            first_name='Jane',
            last_name_1='Doe',
            last_name_2='Smith',
            email='jane.doe@example.com',
            phone='0987654321'
        )
        retrieved_user = UserService.get_user_by_id(user.id)
        self.assertEqual(retrieved_user.id, user.id)
        self.assertEqual(retrieved_user.email, 'jane.doe@example.com')

    def test_update_user(self):
        """Prueba la actualización de un usuario existente."""
        user = UserService.create_user(
            first_name='Alice',
            last_name_1='Johnson',
            last_name_2='Williams',
            email='alice.johnson@example.com',
            phone='1122334455'
        )
        updated_user = UserService.update_user(user.id, first_name='Alicia')
        self.assertEqual(updated_user.first_name, 'Alicia')

    def test_delete_user(self):
        """Prueba la eliminación de un usuario."""
        user = UserService.create_user(
            first_name='Bob',
            last_name_1='Brown',
            last_name_2='Jones',
            email='bob.brown@example.com',
            phone='6677889900'
        )
        result = UserService.delete_user(user.id)
        self.assertTrue(result)

    def test_create_course(self):
        """Prueba la creación de un nuevo curso."""
        course = CourseService.create_course(
            title='Python Programming',
            description='Learn the basics of Python programming.',
            duration='4 weeks'
        )
        self.assertIsNotNone(course.id)
        self.assertEqual(course.title, 'Python Programming')

    def test_get_course_by_id(self):
        """Prueba la obtención de un curso por su ID."""
        course = CourseService.create_course(
            title='Data Science',
            description='Introduction to Data Science.',
            duration='6 weeks'
        )
        retrieved_course = CourseService.get_course_by_id(course.id)
        self.assertEqual(retrieved_course.id, course.id)

    def test_update_course(self):
        """Prueba la actualización de un curso existente."""
        course = CourseService.create_course(
            title='Web Development',
            description='Learn how to build websites.',
            duration='8 weeks'
        )
        updated_course = CourseService.update_course(course.id, title='Full Stack Development')
        self.assertEqual(updated_course.title, 'Full Stack Development')

    def test_delete_course(self):
        """Prueba la eliminación de un curso."""
        course = CourseService.create_course(
            title='Machine Learning',
            description='Basics of machine learning.',
            duration='5 weeks'
        )
        result = CourseService.delete_course(course.id)
        self.assertTrue(result)

    def test_create_education(self):
        """Prueba la creación de una nueva educación."""
        education = EducationService.create_education(
            institution='University of Example',
            degree='Bachelor of Science',
            field_of_study='Computer Science',
            start_date='2015-09-01',
            end_date='2019-05-15'
        )
        self.assertIsNotNone(education.id)
        self.assertEqual(education.degree, 'Bachelor of Science')

    def test_get_education_by_id(self):
        """Prueba la obtención de educación por su ID."""
        education = EducationService.create_education(
            institution='Sample University',
            degree='Master of Science',
            field_of_study='Data Science',
            start_date='2020-09-01',
            end_date='2022-05-15'
        )
        retrieved_education = EducationService.get_education_by_id(education.id)
        self.assertEqual(retrieved_education.id, education.id)

    def test_update_education(self):
        """Prueba la actualización de educación existente."""
        education = EducationService.create_education(
            institution='Another University',
            degree='Associate Degree',
            field_of_study='Information Technology',
            start_date='2013-09-01',
            end_date='2015-05-15'
        )
        updated_education = EducationService.update_education(education.id, degree='Diploma')
        self.assertEqual(updated_education.degree, 'Diploma')

    def test_delete_education(self):
        """Prueba la eliminación de educación."""
        education = EducationService.create_education(
            institution='Example Institute',
            degree='PhD',
            field_of_study='Artificial Intelligence',
            start_date='2016-09-01',
            end_date='2020-05-15'
        )
        result = EducationService.delete_education(education.id)
        self.assertTrue(result)

    def test_create_job(self):
        """Prueba la creación de un nuevo trabajo."""
        job = JobService.create_job(
            title='Software Engineer',
            company='Tech Company',
            start_date='2021-01-01',
            end_date='2023-12-31',
            description='Developing software applications.'
        )
        self.assertIsNotNone(job.id)
        self.assertEqual(job.title, 'Software Engineer')

    def test_get_job_by_id(self):
        """Prueba la obtención de trabajo por su ID."""
        job = JobService.create_job(
            title='Data Analyst',
            company='Data Corp',
            start_date='2020-01-01',
            end_date='2022-12-31',
            description='Analyzing data trends and insights.'
        )
        retrieved_job = JobService.get_job_by_id(job.id)
        self.assertEqual(retrieved_job.id, job.id)

    def test_update_job(self):
        """Prueba la actualización de trabajo existente."""
        job = JobService.create_job(
            title='Product Manager',
            company='Product Co',
            start_date='2019-01-01',
            end_date='2021-12-31',
            description='Managing product development.'
        )
        updated_job = JobService.update_job(job.id, title='Senior Product Manager')
        self.assertEqual(updated_job.title, 'Senior Product Manager')

    def test_delete_job(self):
        """Prueba la eliminación de trabajo."""
        job = JobService.create_job(
            title='Web Developer',
            company='Web Solutions',
            start_date='2018-01-01',
            end_date='2020-12-31',
            description='Building websites.'
        )
        result = JobService.delete_job(job.id)
        self.assertTrue(result)

    def test_create_project(self):
        """Prueba la creación de un nuevo proyecto."""
        project = ProjectService.create_project(
            title='Portfolio Website',
            description='A personal portfolio website.',
            start_date='2022-01-01',
            end_date='2022-06-01'
        )
        self.assertIsNotNone(project.id)
        self.assertEqual(project.title, 'Portfolio Website')

    def test_get_project_by_id(self):
        """Prueba la obtención de un proyecto por su ID."""
        project = ProjectService.create_project(
            title='Data Visualization Dashboard',
            description='A dashboard for data visualization.',
            start_date='2021-01-01',
            end_date='2021-12-31'
        )
        retrieved_project = ProjectService.get_project_by_id(project.id)
        self.assertEqual(retrieved_project.id, project.id)

    def test_update_project(self):
        """Prueba la actualización de un proyecto existente."""
        project = ProjectService.create_project(
            title='Mobile App Development',
            description='Developing a mobile application.',
            start_date='2020-01-01',
            end_date='2020-12-31'
        )
        updated_project = ProjectService.update_project(project.id, title='Advanced Mobile App Development')
        self.assertEqual(updated_project.title, 'Advanced Mobile App Development')

    def test_delete_project(self):
        """Prueba la eliminación de un proyecto."""
        project = ProjectService.create_project(
            title='Website Redesign',
            description='Redesigning an existing website.',
            start_date='2019-01-01',
            end_date='2019-12-31'
        )
        result = ProjectService.delete_project(project.id)
        self.assertTrue(result)

    def test_create_skill(self):
        """Prueba la creación de una nueva habilidad."""
        skill = SkillService.create_skill(
            name='Python',
            level='Intermediate'
        )
        self.assertIsNotNone(skill.id)
        self.assertEqual(skill.name, 'Python')

    def test_get_skill_by_id(self):
        """Prueba la obtención de habilidad por su ID."""
        skill = SkillService.create_skill(
            name='JavaScript',
            level='Advanced'
        )
        retrieved_skill = SkillService.get_skill_by_id(skill.id)
        self.assertEqual(retrieved_skill.id, skill.id)

    def test_update_skill(self):
        """Prueba la actualización de habilidad existente."""
        skill = SkillService.create_skill(
            name='Java',
            level='Beginner'
        )
        updated_skill = SkillService.update_skill(skill.id, level='Intermediate')
        self.assertEqual(updated_skill.level, 'Intermediate')

    def test_delete_skill(self):
        """Prueba la eliminación de habilidad."""
        skill = SkillService.create_skill(
            name='C++',
            level='Expert'
        )
        result = SkillService.delete_skill(skill.id)
        self.assertTrue(result)

    def test_create_social_link(self):
        """Prueba la creación de un nuevo enlace social."""
        social_link = SocialLinkService.create_social_link(
            platform='LinkedIn',
            url='https://linkedin.com/in/example'
        )
        self.assertIsNotNone(social_link.id)
        self.assertEqual(social_link.platform, 'LinkedIn')

    def test_get_social_link_by_id(self):
        """Prueba la obtención de un enlace social por su ID."""
        social_link = SocialLinkService.create_social_link(
            platform='Twitter',
            url='https://twitter.com/example'
        )
        retrieved_social_link = SocialLinkService.get_social_link_by_id(social_link.id)
        self.assertEqual(retrieved_social_link.id, social_link.id)

    def test_update_social_link(self):
        """Prueba la actualización de enlace social existente."""
        social_link = SocialLinkService.create_social_link(
            platform='GitHub',
            url='https://github.com/example'
        )
        updated_social_link = SocialLinkService.update_social_link(social_link.id, url='https://github.com/new_example')
        self.assertEqual(updated_social_link.url, 'https://github.com/new_example')

    def test_delete_social_link(self):
        """Prueba la eliminación de enlace social."""
        social_link = SocialLinkService.create_social_link(
            platform='Facebook',
            url='https://facebook.com/example'
        )
        result = SocialLinkService.delete_social_link(social_link.id)
        self.assertTrue(result)

    def test_create_template(self):
        """Prueba la creación de una nueva plantilla."""
        template = TemplateService.create_template(
            title='CV Template',
            content='This is a sample CV template.'
        )
        self.assertIsNotNone(template.id)
        self.assertEqual(template.title, 'CV Template')

    def test_get_template_by_id(self):
        """Prueba la obtención de una plantilla por su ID."""
        template = TemplateService.create_template(
            title='Resume Template',
            content='This is a sample resume template.'
        )
        retrieved_template = TemplateService.get_template_by_id(template.id)
        self.assertEqual(retrieved_template.id, template.id)

    def test_update_template(self):
        """Prueba la actualización de plantilla existente."""
        template = TemplateService.create_template(
            title='Cover Letter Template',
            content='This is a sample cover letter template.'
        )
        updated_template = TemplateService.update_template(template.id, title='Updated Cover Letter Template')
        self.assertEqual(updated_template.title, 'Updated Cover Letter Template')

    def test_delete_template(self):
        """Prueba la eliminación de plantilla."""
        template = TemplateService.create_template(
            title='Invoice Template',
            content='This is a sample invoice template.'
        )
        result = TemplateService.delete_template(template.id)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
