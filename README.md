# Weather Pipeline - Walter Martinez Perales

ETL pipeline en Python para extraer datos del clima desde la API de OpenWeatherMap, transformarlos y cargarlos en PostgreSQL.

## Estructura
```
weather-pipeline/
│ pipeline.py
│ extract.py
│ transform.py
│ load.py
│ config.py
│ logger_config.py
│ requirements.txt
│ .gitignore
└── logs/
```

## Tecnologías
- Python
- PostgreSQL
- SQLAlchemy
- Pandas
- OpenWeatherMap API

## Configuración
1. Clonar este repositorio.
2. Crear un archivo `.env` en la raíz con las variables:
```
API_KEY=tu_api_key
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
DB_PORT=5432
DB_NAME=nombre_bd
```

4. Crear entorno virtual e instalar dependencias:
python -m venv venv
venv\Scripts\activate # Windows
pip install -r requirements.txt

5. Ejecutar el pipeline:
python pipeline.py

## Salida
- Los datos se guardan en la tabla `weather_readings` de la base de datos PostgreSQL.
- Los logs se registran en `logs/weather_pipeline.log`.
