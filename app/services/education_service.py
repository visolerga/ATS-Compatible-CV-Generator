# app/services/education_service.py

from app.models import Education
from peewee import DoesNotExist

class EducationService:
    @staticmethod
    def create_education(user_id, degree, institution, start_date, end_date=None):
        """Crea una nueva educación asociada a un usuario."""
        education = Education.create(
            user_id=user_id,
            degree=degree,
            institution=institution,
            start_date=start_date,
            end_date=end_date
        )
        return education

    @staticmethod
    def get_education_by_id(education_id):
        """Obtiene una educación por su ID."""
        try:
            return Education.get(Education.id == education_id)
        except DoesNotExist:
            return None

    @staticmethod
    def update_education(education_id, **kwargs):
        """Actualiza la información de una educación existente."""
        education = EducationService.get_education_by_id(education_id)
        if education:
            for key, value in kwargs.items():
                setattr(education, key, value)
            education.save()
            return education
        return None

    @staticmethod
    def delete_education(education_id):
        """Elimina una educación de la base de datos."""
        education = EducationService.get_education_by_id(education_id)
        if education:
            education.delete_instance()
            return True
        return False
