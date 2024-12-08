import logging
from logging.handlers import RotatingFileHandler
import os
# from app.config.config import Config as config
from app.version import VERSION

# Configuración del directorio de logs
LOG_DIR = os.path.join("./logs")
os.makedirs(LOG_DIR, exist_ok=True)

# LOG_FILE = os.path.join(LOG_DIR, f"{Config.APP_ENV}.log")  # Un log por entorno
# LOG_FILE = os.path.join(LOG_DIR, f"{config.APP_ENV}.log")  # Un log por entorno
LOG_FILE = os.path.join(LOG_DIR, f"unico.log")  # Un log por entorno

# Configurar logging con un archivo rotativo
logging.basicConfig(
    level=logging.INFO,  # Cambiar a DEBUG en desarrollo si es necesario
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[
        RotatingFileHandler(LOG_FILE, maxBytes=5 * 1024 * 1024, backupCount=5),
        logging.StreamHandler()  # También muestra en consola
    ]
)

# Logger para el proyecto
# logger = logging.getLogger(Config.APP_NAME)
# logger.info(f"Inicializando {Config.APP_NAME} - Versión {VERSION}")
