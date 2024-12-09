# app/services/skill_service.py

from app.models import Skill
from peewee import DoesNotExist

class SkillService:
    @staticmethod
    def create_skill(name, source_type, user_id, source_id=None):
        """Crea una nueva habilidad asociada a un usuario."""
        skill = Skill.create(
            name=name,
            source_type=source_type,
            source_id=source_id,
            user_id=user_id
        )
        return skill

    @staticmethod
    def get_skill_by_id(skill_id):
        """Obtiene una habilidad por su ID."""
        try:
            return Skill.get(Skill.id == skill_id)
        except DoesNotExist:
            return None

    @staticmethod
    def update_skill(skill_id, **kwargs):
        """Actualiza la información de una habilidad existente."""
        skill = SkillService.get_skill_by_id(skill_id)
        if skill:
            for key, value in kwargs.items():
                setattr(skill, key, value)
            skill.save()
            return skill
        return None

    @staticmethod
    def delete_skill(skill_id):
        """Elimina una habilidad de la base de datos."""
        skill = SkillService.get_skill_by_id(skill_id)
        if skill:
            skill.delete_instance()
            return True
        return False
