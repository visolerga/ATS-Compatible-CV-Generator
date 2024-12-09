# app/services/social_link_service.py

from app.models import SocialLink
from peewee import DoesNotExist

class SocialLinkService:
    @staticmethod
    def create_social_link(user_id, platform, url):
        """Crea un nuevo enlace social asociado a un usuario."""
        social_link = SocialLink.create(
            user_id=user_id,
            platform=platform,
            url=url
        )
        return social_link

    @staticmethod
    def get_social_link_by_id(link_id):
        """Obtiene un enlace social por su ID."""
        try:
            return SocialLink.get(SocialLink.id == link_id)
        except DoesNotExist:
            return None

    @staticmethod
    def update_social_link(link_id, **kwargs):
        """Actualiza la información de un enlace social existente."""
        link = SocialLinkService.get_social_link_by_id(link_id)
        if link:
            for key, value in kwargs.items():
                setattr(link, key, value)
            link.save()
            return link
        return None

    @staticmethod
    def delete_social_link(link_id):
        """Elimina un enlace social de la base de datos."""
        link = SocialLinkService.get_social_link_by_id(link_id)
        if link:
            link.delete_instance()
            return True
        return False
