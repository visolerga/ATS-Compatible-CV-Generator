# app/services/user_service.py

from app.models import User
from peewee import DoesNotExist

class UserService:
    @staticmethod
    def create_user(first_name, last_name_1, last_name_2, email, phone, address=None, city=None, state=None, postal_code=None, country=None):
        """Crea un nuevo usuario en la base de datos."""
        user = User.create(
            first_name=first_name,
            last_name_1=last_name_1,
            last_name_2=last_name_2,
            email=email,
            phone=phone,
            address=address,
            city=city,
            state=state,
            postal_code=postal_code,
            country=country
        )
        return user

    @staticmethod
    def get_user_by_id(user_id):
        """Obtiene un usuario por su ID."""
        try:
            return User.get(User.id == user_id)
        except DoesNotExist:
            return None

    @staticmethod
    def update_user(user_id, **kwargs):
        """Actualiza la información de un usuario existente."""
        user = UserService.get_user_by_id(user_id)
        if user:
            for key, value in kwargs.items():
                setattr(user, key, value)
            user.save()
            return user
        return None

    @staticmethod
    def delete_user(user_id):
        """Elimina un usuario de la base de datos."""
        user = UserService.get_user_by_id(user_id)
        if user:
            user.delete_instance()
            return True
        return False
