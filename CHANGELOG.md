# Changelog

All notable changes to this project will be documented in this file.

## [0.2.0] - 2026-02-28

### Added
- Global filter sidebar for **School Type** and **Parental Education Level**.
- Shared reactive calculation `filtered_data()` used across multiple outputs.
- KPI value boxes for **AVG Exam Score**, **AVG Hours Studied**, and **AVG Attendance**.
- Three interactive Altair visualizations:
  - Study habits vs. performance scatter plot with LOESS trend line
  - Exam score distribution by family income (boxplot)
  - Average exam score by parental involvement (bar chart)

### Changed
- Cleaned dataset by dropping rows missing key filter fields (`School_Type`, `Parental_Education_Level`) to ensure filters behave consistently.
- Organized layout into a sidebar + KPI row + charts for faster “at-a-glance” interpretation.

### Fixed
- Handled empty filter selections by returning an empty dataframe and displaying `"N/A"` for KPIs (prevents errors).

### Known Issues
- Color palette consistency across charts can be improved for accessibility/polish in M3.
- Empty selection states show blank charts; could be improved with clearer user guidance messaging.

### Reflection

**Job stories status:**

- Fully implemented:
  - Filtering by School Type and Parental Education Level with synchronized updates across all outputs.
  - KPI summaries (average exam score, hours studied, attendance).
  - Visualization of study effort (scatter plot with LOESS trend).
  - Comparison of contextual factors (income distribution and parental involvement).

- Partially implemented:
  - Broader comparisons across additional contextual variables (e.g., tutoring sessions, resource access) planned for future expansion.

- Pending for M3:
  - Additional filtering dimensions.
  - Enhanced analytical views and deeper comparison tools.

**Layout vs. M1 sketch and M2 specification:**

The final layout preserves the original M1 concept of a global filter panel combined with summary metrics and core visualizations. Minor refinements were made to improve clarity and visual hierarchy (e.g., grouping KPIs above charts for quick interpretation). These refinements do not change the underlying component structure and are reflected in the updated M2 specification.