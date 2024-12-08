import os
from dotenv import load_dotenv
# Log de la configuración cargada
# from ..utils.logging_config import logger
from app.utils.logging_config import logging


class Config:
    """Clase para gestionar las configuraciones de la aplicación."""
    # Cargar el archivo .env
    load_dotenv()

    # Configuración General
    APP_NAME = os.getenv('APP_NAME', 'DefaultAppName')
    APP_ENV = os.getenv('APP_ENV', 'development')

    # Configuración de Base de Datos
    DB_NAME = os.getenv('DB_NAME', 'database.db')
    DB_PATH = os.getenv('DB_PATH', './data/')
    DB_FULL_PATH = os.path.join(DB_PATH, DB_NAME)

    # Configuración de Exportaciones
    EXPORT_PATH = os.getenv('EXPORT_PATH', './exports/')
    TEMPLATES_PATH = os.getenv('TEMPLATES_PATH', './templates/')

    @staticmethod
    def ensure_directories():
        """Crea los directorios necesarios si no existen."""
        os.makedirs(Config.DB_PATH, exist_ok=True)
        os.makedirs(Config.EXPORT_PATH, exist_ok=True)
        os.makedirs(Config.TEMPLATES_PATH, exist_ok=True)

# Asegurarse de que las carpetas necesarias existan al cargar la configuración
Config.ensure_directories()

# # Logging de la configuración cargada
logging.info(f"Configuración cargada: {Config.APP_NAME} en entorno {Config.APP_ENV}")
logging.info(f"Base de datos en: {Config.DB_FULL_PATH}")

# Depuración opcional en la consola
print("Valores cargados desde .env:")
print(f"APP_NAME: {Config.APP_NAME}")
print(f"DB_NAME: {Config.DB_NAME}")