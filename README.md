# 8730-assignment

A comprehensive data analysis project for COMP 8730.

## Project Overview

This project focuses on [brief description of your analysis goals].

## Repository Structure

```
8730-assignment/
├── README.md                 # Project documentation
├── .gitignore               # Git ignore rules
├── requirements.txt         # Python dependencies
│
├── data/                    # Data directory
│   ├── raw/                # Raw data (never modified)
│   ├── processed/          # Cleaned and processed data
│   └── external/           # External data sources
│
├── scripts/                 # Python scripts
│   ├── data_collection.py  # Data collection and import
│   ├── cleaning.py         # Data cleaning and preprocessing
│   ├── analysis.py         # Analysis scripts
│   ├── visualization.py    # Visualization generation
│   └── utils.py            # Utility functions
│
├── notebooks/              # Jupyter notebooks for exploration
│
├── sql/                     # SQL queries and database scripts
│
├── mongodb/                # MongoDB scripts and configurations
│
├── reports/                # Generated reports and outputs
│   └── Figures/           # Generated figures and plots
│
├── docs/                   # Documentation
│
├── images/                 # Image assets
│
└── video/                  # Video files or documentation
```

## Getting Started

### Prerequisites

- Python 3.8+
- pip or conda

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Ishtiak06/8730-assignment.git
cd 8730-assignment
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Usage

#### Data Processing
```bash
# Collect raw data
python scripts/data_collection.py

# Clean and process data
python scripts/cleaning.py

# Run analysis
python scripts/analysis.py

# Generate visualizations
python scripts/visualization.py
```

#### Jupyter Notebooks
```bash
jupyter notebook notebooks/
```

## Data Sources

- **MongoDB**: Active dataset imports
- **CSV**: External data files in `data/external/`

## Project Structure Details

### `/data`
- `raw/`: Original, immutable data files
- `processed/`: Cleaned data ready for analysis
- `external/`: Third-party or reference data

### `/scripts`
- Modular Python scripts for reproducibility
- Import reusable functions from `utils.py`

### `/notebooks`
- Exploratory data analysis (EDA)
- Prototyping and experimentation

### `/sql` and `/mongodb`
- Database queries and connection scripts
- Schema definitions

### `/reports`
- Generated analysis reports
- Output visualizations and figures

## Contributors

- Ishtiak06
- nov-cpu
- satabdee94

## License

[Add license information if applicable]

## Notes

- Always keep raw data in `data/raw/` unchanged
- Document your analysis in notebooks and README
- Update this README as the project evolves