"""
Data analysis script for statistical and exploratory analysis.
"""

import logging
import pandas as pd
from utils import get_data_paths, log_info, log_error

logger = logging.getLogger(__name__)


def load_processed_data(filename):
    """
    Load processed data for analysis.
    
    Args:
        filename (str): Name of the file in data/processed/
        
    Returns:
        pd.DataFrame: Loaded data
    """
    paths = get_data_paths()
    filepath = paths['processed'] / filename
    log_info(f"Loading processed data from {filepath}")
    return pd.read_csv(filepath)


def descriptive_statistics(df):
    """
    Generate descriptive statistics.
    
    Args:
        df (pd.DataFrame): Data to analyze
        
    Returns:
        dict: Statistical summary
    """
    log_info("Generating descriptive statistics...")
    stats = {
        'shape': df.shape,
        'columns': df.columns.tolist(),
        'dtypes': df.dtypes.to_dict(),
        'missing_values': df.isnull().sum().to_dict(),
    }
    return stats


def correlation_analysis(df):
    """
    Analyze correlations between variables.
    
    Args:
        df (pd.DataFrame): Data to analyze
        
    Returns:
        pd.DataFrame: Correlation matrix
    """
    log_info("Computing correlations...")
    return df.corr()


def main():
    """Main execution function."""
    try:
        log_info("Analysis completed successfully!")
    except Exception as e:
        log_error(f"Error during analysis: {str(e)}")
        raise


if __name__ == "__main__":
    main()