# app/services/template_service.py

from app.models import Template
from peewee import DoesNotExist

class TemplateService:
    @staticmethod
    def create_template(name, content):
        """Crea una nueva plantilla en la base de datos."""
        template = Template.create(
            name=name,
            content=content
        )
        return template

    @staticmethod
    def get_template_by_id(template_id):
        """Obtiene una plantilla por su ID."""
        try:
            return Template.get(Template.id == template_id)
        except DoesNotExist:
            return None

    @staticmethod
    def update_template(template_id, **kwargs):
        """Actualiza la información de una plantilla existente."""
        template = TemplateService.get_template_by_id(template_id)
        if template:
            for key, value in kwargs.items():
                setattr(template, key, value)
            template.save()
            return template
        return None

    @staticmethod
    def delete_template(template_id):
        """Elimina una plantilla de la base de datos."""
        template = TemplateService.get_template_by_id(template_id)
        if template:
            template.delete_instance()
            return True
        return False
