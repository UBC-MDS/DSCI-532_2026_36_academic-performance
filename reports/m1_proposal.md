## Motivation and Purpose

> **Our role:**
> 
> **Target audience:**
>
> 

## Description of the Data

> 

## Research Questions & Usage Scenarios

### Usage Scenario
> Jane is a concerned parent of a high school student, and she wants to support her son's education and academic performance but is not sure if she should focus more on hiring tutors or enforcing strict bedtimes.
>
> Jane accesses the dashboard of academic performance and navigates to the "Lifestyle vs. Performance" tab. She uses the filters to select students with high `parental_involvement` to see a relevant baseline. She interacts with a scatter plot comparing sleep_hours against exam_score. She notices a trend where students getting 8+ hours of sleep consistently outperform those getting less than 6, regardless of access_to_resources.
> 
> Jane decides to prioritize an earlier curfew for her child rather than purchasing expensive extra resources, data-backing her parenting decision.
> 

### User Stories

> **User Story 1:**
> As a parent, I want to visualize the correlation between hours of sleep and final grades in order to determine if enforcing a stricter bedtime is a more effective strategy than increasing study hours.
>
> **User Story 2:**
> 
>
> **User Story 3:**
> 

### Jobs to Be Done
*...or as Jobs to Be Done:*

> **JTBD 1:**
> **Situation:** When I am reviewing monthly attendance reports...
> **Motivation:** ...I want to separate routine absences from systemic issues...
> **Outcome:** ...so I can allocate intervention budget to the right patient groups.
>
> **JTBD 2:**
> **Situation:** When investigating a spike in no-shows...
> **Motivation:** ...I want to see if specific physical disabilities correlate with absenteeism...
> **Outcome:** ...so I can propose targeted transportation support services.
>
> **JTBD 3:**
> **Situation:** When planning clinic hours...
> **Motivation:** ...I want to see if appointments on Mondays or Fridays are missed more often...
> **Outcome:** ...so I can optimize the scheduling grid.

## Exploratory Data Analysis

>
> **Analysis:** (See full [EDA Notebook](../notebooks/eda_analysis.ipynb)) To address User Story 1, we created two visualizations that analyze the relationship between hours of sleep and academic performance:
> - Scatter Plot with Trend Lines: We plotted a scatter plot of `Exam Score` against `Hours of Sleep`, faceted by `Resource Access` to determine if more hours of sleep is correlated with higher exam scores.
> - Grouped Bar Chart: We aggregated average exam scores into three sleep categories (< 6, 6-8, and > 8 hours) to check for broader patterns across different levels of access to resources.

> **Reflection:** Both visualizations show a negligible correlation between sleep duration and exam scores. All three regression lines on the scatter plot have small slopes. The grouped bar chart shows nearly identical average exam scores regardless of whether a student sleeps less than 6 hours or more than 8 hours. This exploration suggests that it might be better for the parents of students to shift their focus away from sleep duration and other explanatory variables, such as `Access_to_Resources`, might have a higher impact on academic performance. These observations are purely descriptive; further statistical testing is necessary to validate these patterns and draw robust inferential conclusions regarding the population.

## App Sketch & Description

![Dashboard](../img/sketch.png "App Sketch")

> 
