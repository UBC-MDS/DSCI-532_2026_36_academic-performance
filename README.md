# DSCI-532_2026_36_academic-performance
# Academic Performance Dashboard

This project develops an interactive dashboard using **Shiny for Python** to explore factors associated with student academic performance.

The goal is to create a human-centered, interactive decision-support tool that enables users to explore patterns in student outcomes through filtering and visualization.

---

## Project Structure

DSCI-532_2026_36_academic-performance/

- src/                # Shiny application (app.py)
- data/raw/           # Raw dataset
- notebooks/          # Exploratory Data Analysis (EDA)
- reports/            # Proposal document
- img/                # Dashboard sketch
- environment.yml     # Project dependencies
- README.md

---

## Setup Instructions

### 1. Clone the repository

git clone https://github.com/UBC-MDS/DSCI-532_2026_36_academic-performance.git  
cd DSCI-532_2026_36_academic-performance

### 2. Create the conda environment

conda env create -f environment.yml  
conda activate dsci-532-m1

### 3. Run the Shiny dashboard locally

python src/app.py

After running, open the URL shown in the terminal (typically http://127.0.0.1:8000).

---

## Milestone 1 Status

- Shiny app skeleton implemented
- Sidebar layout structured
- Value boxes and cards added as placeholders
- Environment configuration completed
- Ready for further development in Milestone 2