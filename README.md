# DSCI-532_2026_36_academic-performance

# Academic Performance Dashboard

## Live App

- **Stable Release (main):** https://mkmetiuk-dsci-532-2026-36-academic-performance.share.connect.posit.cloud
- **Preview Build (dev):** https://mkmetiuk-dev.share.connect.posit.cloud

---

## Demo

![Demo of Academic Performance Dashboard](img/demo.gif)

---

## Overview

This project develops an interactive dashboard using **Shiny for Python** to explore factors associated with student academic performance.

The dashboard supports:

- Filtering students by **School Type** and **Parental Education Level**
- Filtering students by **Parental Involvment Level**. To filter click on corresponding bar on **Impact of Parental Involvement** bar chart.
- Viewing real-time KPI summaries:
  - Average Exam Score
  - Average Hours Studied
  - Average Attendance
- Exploring relationships between:
  - Study habits and exam performance (scatter + LOESS)
  - Family income and score distribution (boxplot)
  - Parental involvement and average performance (bar chart) - Interactive! Click on each bar to filter.

### AI Assistant

The dashboard includes an AI-powered assistant that allows users to explore the dataset using natural language queries.

Users can:
- Ask questions about the dataset (e.g., "Show students with high exam scores")
- Filter data through conversational queries
- View results in a table within the app
- Download AI-generated filtered datasets directly from the interface

The goal is to support data-driven educational decision-making for school administrators and families. The dashboard is publicly deployed on Posit Connect Cloud.

---

## New Features (Milestone 4)

- AI Assistant powered by QueryChat for natural language data exploration  
- Customizable explanation styles for different user needs  
- Downloadable AI-generated filtered datasets  
- Data pipeline upgraded to **Parquet + DuckDB** for efficient querying  
- Reactive filtering using **Ibis + @reactive.calc** for lazy evaluation  
- UI improvements including tooltips and consistent styling  
- Automated testing with Playwright (UI tests) and pytest (unit tests)  

---

## Installation (for contributors)

```bash
git clone https://github.com/UBC-MDS/DSCI-532_2026_36_academic-performance.git
cd DSCI-532_2026_36_academic-performance

conda env create -f environment.yml
conda activate dsci-532-m1

cd src
shiny run app.py
```

---

## Project Structure

```text
DSCI-532_2026_36_academic-performance/
├── src/              # Shiny application (app.py)
├── data/             # Raw and processed datasets (Parquet)
├── tests/            # Unit tests (pytest) and UI tests (Playwright)
├── notebooks/        # EDA and analysis
├── reports/          # Project documents (M1–M4)
├── img/              # Demo and design assets
├── CHANGELOG.md
├── CONTRIBUTING.md
├── environment.yml
└── README.md
```

---

## Running Tests

Run the following command from the root directory:

```bash
pytest tests/ -v
```

This command runs both UI and unit tests for the dashboard:

- Playwright tests verify key user interactions, such as filtering inputs updating charts and outputs correctly.
- pytest unit tests verify core data processing logic, including filtering and aggregation behavior.

These tests ensure that the dashboard functions as expected and help detect issues if core logic or UI behavior changes. All tests are expected to pass in a clean environment.

---

## AI Assistant Usage

The AI Assistant allows users to explore the dataset using natural language queries through the QueryChat interface.

Users can:
- Ask questions to filter or summarize the dataset (e.g., "Show students with exam scores above 80")
- Interactively refine queries based on results
- View the filtered results in a table within the app
- Download the resulting dataset as a CSV file

Example queries:
- "Show students with exam scores above 80"
- "Which school type studies the most hours?"
- "Filter to students with postgraduate parents"

The assistant supports flexible data exploration and helps users quickly generate insights without writing code.

---


## Team Members
- Karan Bains
- Mykhailo Kmetiuk
- Gurveer Madurai
- Siting Wang
