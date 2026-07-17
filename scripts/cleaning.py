"""
Data cleaning and preprocessing script.
"""

import logging
import pandas as pd
from utils import get_data_paths, ensure_directories_exist, log_info, log_error

logger = logging.getLogger(__name__)


def load_raw_data(filename):
    """
    Load raw data from CSV or other formats.
    
    Args:
        filename (str): Name of the file in data/raw/
        
    Returns:
        pd.DataFrame: Loaded data
    """
    paths = get_data_paths()
    filepath = paths['raw'] / filename
    log_info(f"Loading raw data from {filepath}")
    return pd.read_csv(filepath)


def clean_data(df):
    """
    Clean and preprocess the dataframe.
    
    Args:
        df (pd.DataFrame): Raw dataframe
        
    Returns:
        pd.DataFrame: Cleaned dataframe
    """
    log_info("Starting data cleaning...")
    df = df.drop_duplicates()
    df = df.dropna()
    log_info(f"Data cleaning completed. Shape: {df.shape}")
    return df


def save_processed_data(df, filename):
    """
    Save cleaned data to processed directory.
    
    Args:
        df (pd.DataFrame): Cleaned dataframe
        filename (str): Output filename
    """
    paths = get_data_paths()
    filepath = paths['processed'] / filename
    df.to_csv(filepath, index=False)
    log_info(f"Processed data saved to {filepath}")


def main():
    """Main execution function."""
    ensure_directories_exist()
    try:
        log_info("Data cleaning completed successfully!")
    except Exception as e:
        log_error(f"Error during data cleaning: {str(e)}")
        raise


if __name__ == "__main__":
    main()