"""
Utility functions for data collection, cleaning, and analysis.
"""

import logging
from pathlib import Path

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def get_data_paths():
    """
    Get paths to data directories.
    
    Returns:
        dict: Dictionary containing paths to raw, processed, and external data directories
    """
    base_path = Path(__file__).parent.parent
    return {
        'raw': base_path / 'data' / 'raw',
        'processed': base_path / 'data' / 'processed',
        'external': base_path / 'data' / 'external',
        'base': base_path / 'data'
    }


def ensure_directories_exist():
    """Create necessary data directories if they don't exist."""
    paths = get_data_paths()
    for path in paths.values():
        if isinstance(path, Path):
            path.mkdir(parents=True, exist_ok=True)
            logger.info(f"Ensured directory exists: {path}")


def log_info(message):
    """Log info message."""
    logger.info(message)


def log_error(message):
    """Log error message."""
    logger.error(message)


if __name__ == "__main__":
    ensure_directories_exist()