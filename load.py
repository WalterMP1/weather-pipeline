#load.py
from sqlalchemy import create_engine, text
from config import DB_URL
from logger_config import get_logger

logger = get_logger(__name__)

def create_table():
    engine = create_engine(DB_URL)
    create_table_query = """
    CREATE TABLE IF NOT EXISTS weather_readings (
        city VARCHAR(100) NOT NULL,
        country CHAR(2) NOT NULL,
        timestamp_utc TIMESTAMP WITH TIME ZONE NOT NULL,
        timestamp_local TIMESTAMP WITH TIME ZONE,
        temp REAL,
        feels_like_c REAL,
        temp_category VARCHAR(9),
        weather_main VARCHAR(50),
        weather_desc VARCHAR(100),
        PRIMARY KEY (city, timestamp_utc)
    );
    """
    with engine.begin() as conn:
        conn.execute(text(create_table_query))

def load_db(df):
    try:
        engine = create_engine(DB_URL)
        columns = ['city','country','timestamp_utc','timestamp_local','temp','feels_like_c','temp_category','weather_main','weather_desc']
        df_to_insert = df[columns]
        df_to_insert.to_sql('weather_readings', engine, if_exists='append', index=False)
        logger.info("Data loaded into database successfully")
    except Exception as e:
        logger.error(f"Error inserting data into database: {e}", exc_info=True)