import pandas as pd
from logger import get_logger

logger = get_logger()

def load_data(file_path):
    try:
        df = pd.read_excel(file_path)
        logger.info("Data loaded successfully")
        return df
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        raise

def process_data(df):
    summary = df.groupby("Product")["Sales"].sum()
    logger.info("Data processed successfully")
    return summary