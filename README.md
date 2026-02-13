# DSCI-532_2026_36_academic-performance
# Academic Performance Dashboard

This dashboard explores the Student Academic Performance dataset and provides interactive visualizations to support data exploration and decision-making.

The application allows users to examine academic, behavioral, and demographic factors that may influence student performance. The goal is to create a human-centered interactive tool for understanding patterns in student outcomes.

---

## Project Structure

DSCI-532_2026_36_academic-performance/

- src/                # Dash application (app.py)
- data/raw/           # Raw dataset
- notebooks/          # EDA notebooks
- reports/            # Proposal document
- img/                # Dashboard sketch
- environment.yml     # Project dependencies
- README.md

---

## Setup Instructions

### 1. Clone the repository

git clone <repo-link>  
cd DSCI-532_2026_36_academic-performance

### 2. Create the conda environment

conda env create -f environment.yml  
conda activate dsci-532-m1

### 3. Run the dashboard locally

python src/app.py

Then open your browser and go to:

http://127.0.0.1:8050

---

## Milestone 1 Status

- Basic dashboard skeleton implemented  
- Layout placeholders added  
- Environment configuration completed  
- Ready for further development in Milestone 2