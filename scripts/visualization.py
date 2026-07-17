"""
Visualization script for generating charts and plots.
"""

import logging
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from utils import get_data_paths, log_info, log_error

logger = logging.getLogger(__name__)

sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)


def get_report_path():
    """Get path to reports directory."""
    base_path = Path(__file__).parent.parent
    return base_path / 'reports' / 'Figures'


def load_processed_data(filename):
    """
    Load processed data for visualization.
    
    Args:
        filename (str): Name of the file in data/processed/
        
    Returns:
        pd.DataFrame: Loaded data
    """
    paths = get_data_paths()
    filepath = paths['processed'] / filename
    log_info(f"Loading data from {filepath}")
    return pd.read_csv(filepath)


def save_figure(fig, filename):
    """
    Save figure to reports directory.
    
    Args:
        fig: Matplotlib figure object
        filename (str): Output filename
    """
    report_path = get_report_path()
    report_path.mkdir(parents=True, exist_ok=True)
    filepath = report_path / filename
    fig.savefig(filepath, dpi=300, bbox_inches='tight')
    log_info(f"Figure saved to {filepath}")
    plt.close(fig)


def main():
    """Main execution function."""
    try:
        log_info("Visualization completed successfully!")
    except Exception as e:
        log_error(f"Error during visualization: {str(e)}")
        raise


if __name__ == "__main__":
    main()