# app/services/course_service.py

from app.models import Course
from peewee import DoesNotExist

class CourseService:
    @staticmethod
    def create_course(user_id, title, institution=None, completion_date=None):
        """Crea un nuevo curso asociado a un usuario."""
        course = Course.create(
            user_id=user_id,
            title=title,
            institution=institution,
            completion_date=completion_date
        )
        return course

    @staticmethod
    def get_course_by_id(course_id):
        """Obtiene un curso por su ID."""
        try:
            return Course.get(Course.id == course_id)
        except DoesNotExist:
            return None

    @staticmethod
    def update_course(course_id, **kwargs):
        """Actualiza la información de un curso existente."""
        course = CourseService.get_course_by_id(course_id)
        if course:
            for key, value in kwargs.items():
                setattr(course, key, value)
            course.save()
            return course
        return None

    @staticmethod
    def delete_course(course_id):
        """Elimina un curso de la base de datos."""
        course = CourseService.get_course_by_id(course_id)
        if course:
            course.delete_instance()
            return True
        return False
