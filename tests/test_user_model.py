import unittest  # Importamos la librería para escribir pruebas unitarias
from peewee import SqliteDatabase  # Usamos una base de datos SQLite para las pruebas
from app.models.user_model import User  # Importamos el modelo User para probarlo
from app.models.base_model import BaseModel  # BaseModel define la conexión a la base de datos

# Configuramos una base de datos en memoria para las pruebas
test_db = SqliteDatabase(':memory:')  # La base de datos no se guarda en disco, perfecta para testing

class TestUserModel(unittest.TestCase):  # Clase que agrupa las pruebas relacionadas con el modelo User

    @classmethod
    def setUpClass(cls):
        """
        Configuración inicial antes de ejecutar las pruebas:
        - Conectamos la base de datos de prueba.
        - Asociamos el modelo User a esta base de datos.
        - Creamos las tablas necesarias en la base de datos de prueba.
        """
        test_db.bind([User], bind_refs=False, bind_backrefs=False)  # Vinculamos el modelo User con test_db
        test_db.connect()  # Conectamos a la base de datos
        test_db.create_tables([User])  # Creamos las tablas necesarias para el modelo

    @classmethod
    def tearDownClass(cls):
        """
        Limpieza final después de todas las pruebas:
        - Cerramos la conexión a la base de datos.
        """
        test_db.drop_tables([User])  # Eliminamos las tablas creadas
        test_db.close()  # Cerramos la base de datos

    def test_user_creation(self):
        """
        Verifica que un usuario puede ser creado correctamente y
        que sus campos son almacenados correctamente en la base de datos.
        """
        # Crear un usuario de ejemplo
        user = User.create(
            first_name="John",
            last_name_1="Doe",
            last_name_2="Smith",
            email="johndoe@example.com",
            phone="123456789",
            address="123 Main Street",
            city="Springfield",
            state="IL",
            postal_code="62704",
            country="USA",
        )

        # Consultar el usuario creado para verificar sus atributos
        fetched_user = User.get_by_id(user.id)
        self.assertEqual(fetched_user.first_name, "John")  # Verifica que el nombre es el esperado
        self.assertEqual(fetched_user.last_name_1, "Doe")  # Verifica el primer apellido
        self.assertEqual(fetched_user.last_name_2, "Smith")  # Verifica el segundo apellido
        self.assertEqual(fetched_user.email, "johndoe@example.com")  # Verifica el email
        self.assertEqual(fetched_user.phone, "123456789")  # Verifica el teléfono

    def test_user_update(self):
        """
        Verifica que se puede actualizar correctamente un usuario existente.
        """
        # Crear un usuario de ejemplo
        user = User.create(first_name="Jane", last_name_1="Doe", email="janedoe@example.com")

        # Actualizar el nombre del usuario
        user.first_name = "Janet"
        user.save()

        # Consultar el usuario actualizado y verificar los cambios
        updated_user = User.get_by_id(user.id)
        self.assertEqual(updated_user.first_name, "Janet")  # Verifica el cambio de nombre

    def test_user_deletion(self):
        """
        Verifica que un usuario puede ser eliminado correctamente de la base de datos.
        """
        # Crear un usuario de ejemplo
        user = User.create(first_name="Alice", last_name_1="Wonderland", email="alice@example.com")

        # Eliminar el usuario
        user_id = user.id
        user.delete_instance()

        # Verificar que ya no existe en la base de datos
        with self.assertRaises(User.DoesNotExist):  # Verifica que intentar obtener el usuario lanza un error
            User.get_by_id(user_id)


# Ejecución del script directamente
if __name__ == "__main__":
    unittest.main()
