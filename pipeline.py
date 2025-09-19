# pipeline.py
from extract import fetch_all
from transform import transform
from load import load_db, create_table
from logger_config import get_logger

logger = get_logger(__name__)

CITIES = ["Monterrey,mx", "San Pedro Garza García,mx", "San Nicolás de los Garza,mx"]

if __name__ == "__main__":
    logger.info("Starting weather pipeline")
    create_table()
    logger.info("Database table ready")
    rows = fetch_all(CITIES)
    df = transform(rows)
    if not df.empty:
        load_db(df)
        logger.info(f"{len(df)} records inserted into the database")
    else:
        logger.info("No new data to insert")
    
    logger.info("Pipeline finished successfully")
