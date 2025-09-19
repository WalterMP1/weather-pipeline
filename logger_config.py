# logger_config.py
import logging
import os

# Carpeta para logs
os.makedirs("logs", exist_ok=True)

# Archivo de log principal
LOG_FILE = os.path.join("logs", "weather_pipeline.log")

# Configuración básica
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,  # Nivel mínimo que se registrará
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Función para obtener logger de cada módulo
def get_logger(name):
    return logging.getLogger(name)
