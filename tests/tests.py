import os
import sys

# Agregar la carpeta raíz del proyecto al path de importación
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../app')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

# print(sys.path)
from app.config.config import Config

def test_config_values():
    """Valida que las variables de configuración se carguen correctamente."""
    print(f"DB_NAME cargado: {Config.DB_NAME}")  # Imprimir el valor cargado
    assert Config.APP_NAME == "ATS-Compatible-CV", "APP_NAME no coincide"
    assert Config.APP_ENV == "development", "APP_ENV no coincide"
    assert Config.DB_NAME == "cv_database.db", "DB_NAME no coincide"
    assert os.path.exists(Config.DB_PATH), "La ruta de la base de datos no existe"
    assert os.path.exists(Config.EXPORT_PATH), "La ruta de exportaciones no existe"
    assert os.path.exists(Config.TEMPLATES_PATH), "La ruta de plantillas no existe"

if __name__ == "__main__":
    test_config_values()
    print("Todas las configuraciones funcionan correctamente.")
