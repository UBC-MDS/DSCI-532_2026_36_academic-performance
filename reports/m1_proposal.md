## Section 1: Motivation and Purpose

**Our role:** Ministry of Education student performance analytics team  

**Target audience:** School staff and educators such as principals, counsellors, and academic coordinators, and parents and students.

Schools constantly need to decide how to spend they limited resources to improve student success. 
These decisions are often made from simple metrics like averages which can hide important information such as attendance patterns, access to resources, motivation and relationships between those.

We propose building an interactive dashboard that helps educational decision makers explore and compare factors associated with exam performance. 
This dashboard will enable users to identify patterns and investigate which variables are most associated with lower exam scores. 
The goal is not to predict individual students, but to provide decision making support: highlight potential areas for intervention, guide policy questions, and support data driven planning.

Our dashboard will also be useful for individual students and their parents looking to improve exam performance by understanding impact of sleep, attendance and other variables. 

## Section 2: Description of the Data

The dataset consists of 6607 rows and 20 columns. We will visualize a student academic performance dataset where each row represents one student and columns represent variables described below. The response is a discrete numeric variable variable `Exam_Score`.

Key explanatory variables are as follows:

- **Academic / effort:** `Hours_Studied`, `Previous_Scores`, `Tutoring_Sessions`
- **Engagement / routine:** `Attendance`, `Sleep_Hours`, `Physical_Activity`, `Extracurricular_Activities`
- **Access / context:** `Access_to_Resources`, `Internet_Access`, `Distance_from_Home`
- **Home / family:** `Parental_Involvement`, `Family_Income`, `Parental_Education_Level`
- **School environment:** `Teacher_Quality`, `School_Type`, `Peer_Influence`
- **Demographics / supports:** `Gender`, `Learning_Disabilities`, `Motivation_Level`

The dashboard will support filtering across some of these categories and comparing distributions of exam scores across groups to help stakeholders understand which combinations of factors are associated with lower performance.


## Section 3: Research Questions & Usage Scenarios

### Persona

**Jordan**, a vice-principal at a mid-sized high school, is responsible for allocating limited resources each term (tutoring seats, counselor check-ins, study skills workshops). 
Jordan needs to understand which student contexts are most commonly associated with low exam performance to prioritize programming.

**Jane** is a concerned parent of a high school student. 
She wants to support her son's education and academic performance but is unsure whether she should focus more on hiring tutors or enforcing stricter sleep routines and lifestyle habits.

### Usage scenarios

**Jordan** opens the dashboard to prepare for next term’s support planning. Jordan first reviews overall performance and then filters to students with low attendance to see how exam scores change across levels of access to resources and parental involvement. 
Jordan notices that low attendance combined with low access to resources is associated with lower exam scores than low attendance alone. Jordan then compares whether tutoring sessions appear to narrow that gap across groups. 
Based on these patterns, Jordan prioritizes after-school tutoring and resource support (e.g., device lending or internet access initiatives) for student groups that appear most disadvantaged.

**Jane** accesses the dashboard and navigates to the "Lifestyle vs. Performance" section. She uses filters to select students with high Parental Involvement to establish a relevant baseline for families similar to hers.
She then interacts with a scatter plot comparing sleep hours against exam score. Jane notices a clear upward trend: students getting 8 or more hours of sleep consistently outperform those getting fewer than 6 hours, regardless of Access to Resources.
Rather than investing in expensive tutoring or additional academic resources, Jane decides to prioritize enforcing an earlier bedtime. The dashboard provides her with data-backed confidence in her parenting decision.

### User Stories 

1. **As a school principal**, I want to filter students by attendance and access to resources so that I can identify groups that may need targeted academic support.

2. **As a school principal**, I want to compare exam score distributions across tutoring session counts so that I can evaluate whether tutoring is associated with improved outcomes for different student contexts.

3. **As a parent**, I want to visualize the relationship between sleep hours and exam performance so that I can determine whether lifestyle adjustments may meaningfully impact my child’s academic success.

4. **As a parent**, I want to compare lifestyle factors (sleep, physical activity) against structural factors (resources, tutoring) so that I can decide where to invest time and money.

### JTBD

1. **Situation:** When planning academic support budgets,  
   **Motivation:** I want to identify which student segments are doing poorly and why,  
   **Outcome:** So I can allocate limited school resources effectively.

2. **Situation:** When evaluating whether tutoring programs are working,  
   **Motivation:** I want to compare performance outcomes across tutoring levels and student backgrounds,  
   **Outcome:** So I can justify expanding or restructuring support programs.

3. **Situation:** When deciding how to support my child at home,  
   **Motivation:** I want to understand whether sleep and lifestyle factors are strongly associated with exam performance,  
   **Outcome:** So I can prioritize the most impactful changes.

4. **Situation:** When considering additional financial investments in education,  
   **Motivation:** I want to compare the relative influence of tutoring versus healthy routines,  
   **Outcome:** So I can make cost-effective, data driven parenting decisions.


## Exploratory Data Analysis

>
> **Analysis:** (See full [EDA Notebook](../notebooks/eda_analysis.ipynb)) To address User Story 3, we created two visualizations that analyze the relationship between hours of sleep and academic performance:
> - Scatter Plot with Trend Lines: We plotted a scatter plot of `Exam Score` against `Hours of Sleep`, faceted by `Resource Access` to determine if more hours of sleep is correlated with higher exam scores.
> - Grouped Bar Chart: We aggregated average exam scores into three sleep categories (< 6, 6-8, and > 8 hours) to check for broader patterns across different levels of access to resources.

> **Reflection:** Both visualizations show a negligible correlation between sleep duration and exam scores. All three regression lines on the scatter plot have small slopes. The grouped bar chart shows nearly identical average exam scores regardless of whether a student sleeps less than 6 hours or more than 8 hours. This exploration suggests that it might be better for the parents of students to shift their focus away from sleep duration and other explanatory variables, such as `Access_to_Resources`, might have a higher impact on academic performance. These observations are purely descriptive; further statistical testing is necessary to validate these patterns and draw robust inferential conclusions regarding the population.

## App Sketch & Description

![Dashboard](../img/sketch.png "App Sketch")

> 
