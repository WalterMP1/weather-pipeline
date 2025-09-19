#transform.py
import pandas as pd
from logger_config import get_logger

logger = get_logger(__name__)

def transform(rows):
    try:
        logger.info("Starting data transformation")
        df = pd.DataFrame(rows)
        logger.info(f"Received {len(df)} records")
        
        df['timestamp_utc'] = pd.to_datetime(df['timestamp_utc'], utc=True)
        # Convertimos a hora local
        df['timestamp_local'] = df['timestamp_utc'].dt.tz_convert('America/Mexico_City')

        before = len(df)
        df = df.drop_duplicates(subset=['city','timestamp_utc'])
        after = len(df)
        logger.info(f"Removed {before - after} duplicates, remaining {after}")
        
        def classify_temp(temp):
            if temp < 10:
                return "cold"
            if temp <= 25:
                return "temperate"
            else:
                return "hot"
        
        df['temp_category'] = df['feels_like_c'].apply(classify_temp)
        logger.info("Data transformation completed successfully")
        return df
    
    except Exception as e:
        logger.error(f"Error in transformation: {e}", exc_info=True)
        raise
