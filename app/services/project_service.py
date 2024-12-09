# app/services/project_service.py

from app.models import Project
from peewee import DoesNotExist

class ProjectService:
    @staticmethod
    def create_project(user_id, title, description=None, url=None):
        """Crea un nuevo proyecto asociado a un usuario."""
        project = Project.create(
            user_id=user_id,
            title=title,
            description=description,
            url=url
        )
        return project

    @staticmethod
    def get_project_by_id(project_id):
        """Obtiene un proyecto por su ID."""
        try:
            return Project.get(Project.id == project_id)
        except DoesNotExist:
            return None

    @staticmethod
    def update_project(project_id, **kwargs):
        """Actualiza la información de un proyecto existente."""
        project = ProjectService.get_project_by_id(project_id)
        if project:
            for key, value in kwargs.items():
                setattr(project, key, value)
            project.save()
            return project
        return None

    @staticmethod
    def delete_project(project_id):
        """Elimina un proyecto de la base de datos."""
        project = ProjectService.get_project_by_id(project_id)
        if project:
            project.delete_instance()
            return True
        return False
