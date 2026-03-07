import pandas as pd
import altair as alt
import numpy as np
from shiny import App, ui, render, reactive
from shinywidgets import output_widget, render_widget
from pathlib import Path

alt.data_transformers.disable_max_rows()

# load in data 
APP_DIR = Path(__file__).resolve().parent
DATA_PATH = APP_DIR.parent / "data" / "StudentPerformanceFactors.csv"

df_raw = pd.read_csv(DATA_PATH)

# only keep rows where our primary filters have values
df = df_raw.dropna(subset=["School_Type", "Parental_Education_Level"]).copy()

income_order = ["Low", "Medium", "High"]
involvement_order = ["Low", "Medium", "High"]

app_ui = ui.page_fluid(
    ui.panel_title("Academic Performance Dashboard"),
    ui.layout_sidebar(
        ui.sidebar(
            ui.h4("Global Filters"),
            ui.input_checkbox_group(
                "school_type",
                "School Type",
                choices=["Public", "Private"],
                selected=["Public", "Private"],
            ),
            ui.input_checkbox_group(
                "parent_edu",
                "Parental Education Level",
                choices=sorted(df["Parental_Education_Level"].unique().tolist()),
                selected=sorted(df["Parental_Education_Level"].unique().tolist()),
            ),
            ui.hr(),
            ui.markdown("**Authors:** Group Project | **DSCI 532**"),
            open="desktop",
        ),

        # TOP CARDS
        ui.layout_columns(
            ui.value_box("AVG Exam Score", ui.output_text("avg_score"), theme="primary"),
            ui.value_box("AVG Hours Studied", ui.output_text("avg_hours")),
            ui.value_box("AVG Attendance", ui.output_text("avg_attendance")),
            fill=False,
        ),

        # CHARTS — no fixed height on cards; charts are fully responsive
        ui.layout_columns(
            ui.card(
                ui.card_header("Study Habits vs. Performance"),
                output_widget("scatter_plot"),
                full_screen=True,
            ),
            ui.card(
                ui.card_header("Attendance vs. Exam Score"),
                output_widget("attendance_scatter"),
                full_screen=True,
            ),
            col_widths=[6, 6],
        ),

        ui.tags.div(style="height: 16px;"),

        ui.layout_columns(
            ui.card(
                ui.card_header("Score Distribution by Family Income"),
                output_widget("income_boxplot"),
                full_screen=True,
            ),
            ui.card(
                ui.card_header("Impact of Parental Involvement"),
                output_widget("involvement_bar"),
                full_screen=True,
            ),
            col_widths=[6, 6],
        ),
    ),
)


def server(input, output, session):
    
    @reactive.calc
    def filtered_data():
        if not input.school_type() or not input.parent_edu():
            return df.iloc[0:0] 
            
        return df[
            (df["School_Type"].isin(input.school_type())) &
            (df["Parental_Education_Level"].isin(input.parent_edu()))
        ].copy()

    # KPI output
    @render.text
    def avg_score():
        data = filtered_data()
        if data.empty: return "N/A"
        return f"{data['Exam_Score'].mean():.1f}%"

    @render.text
    def avg_hours():
        data = filtered_data()
        if data.empty: return "N/A"
        return f"{data['Hours_Studied'].mean():.1f} hrs"

    @render.text
    def avg_attendance():
        data = filtered_data()
        if data.empty: return "N/A"
        return f"{data['Attendance'].mean():.1f}%"

    # Responsive theme — no fixed height, width fills container
    def apply_theme(chart):
        return (
            chart.properties(width="container")
            .configure_axis(labelFontSize=14, titleFontSize=16)
            .configure_view(strokeWidth=0)
        )

    @render_widget
    def scatter_plot():
        data = filtered_data()
        if data.empty: return alt.Chart(pd.DataFrame()).mark_text()

        plot_df = data[["Hours_Studied", "Exam_Score"]].dropna()
        base = alt.Chart(plot_df).encode(
            x=alt.X("Hours_Studied:Q", title="Hours Studied"),
            y=alt.Y("Exam_Score:Q", title="Exam Score", scale=alt.Scale(domain=[40, 100])),
        )
        scatter = base.mark_circle(opacity=0.4, color="#21918c")
        line = base.transform_loess("Hours_Studied", "Exam_Score").mark_line(color="red", size=3)
        
        return apply_theme(scatter + line)

    @render_widget
    def income_boxplot():
        data = filtered_data()
        if data.empty: return alt.Chart(pd.DataFrame()).mark_text()

        plot_df = data[["Family_Income", "Exam_Score"]].dropna()
        chart = alt.Chart(plot_df).mark_boxplot(extent="min-max", size=60, clip=True).encode(
            x=alt.X("Family_Income:N", sort=income_order, title="Family Income", axis=alt.Axis(labelAngle=0)),
            y=alt.Y("Exam_Score:Q", title="Exam Score", scale=alt.Scale(domain=[55, 80])),
            color=alt.Color("Family_Income:N", scale=alt.Scale(scheme="viridis"), legend=None),
        )
        return apply_theme(chart)

    @render_widget
    def involvement_bar():
        data = filtered_data()
        if data.empty: return alt.Chart(pd.DataFrame()).mark_text()

        plot_df = data[["Parental_Involvement", "Exam_Score"]].dropna()
        chart = alt.Chart(plot_df).mark_bar(size=80).encode(
            x=alt.X("Parental_Involvement:N", sort=involvement_order, title="Involvement Level", axis=alt.Axis(labelAngle=0)),
            y=alt.Y("mean(Exam_Score):Q", title="Average Exam Score", scale=alt.Scale(domain=[60, 72])),
            color=alt.Color("Parental_Involvement:N", scale=alt.Scale(scheme="viridis"), legend=None),
        )
        return apply_theme(chart)

    @render_widget
    def attendance_scatter():
        data = filtered_data()
        if data.empty: return alt.Chart(pd.DataFrame()).mark_text()

        plot_df = data[["Attendance", "Exam_Score"]].dropna()
        base = alt.Chart(plot_df).encode(
            x=alt.X("Attendance:Q", title="Attendance (%)", scale=alt.Scale(domain=[60, 100])),
            y=alt.Y("Exam_Score:Q", title="Exam Score", scale=alt.Scale(domain=[40, 100])),
        )
        scatter = base.mark_circle(opacity=0.4, color="#21918c")
        line = base.transform_loess("Attendance", "Exam_Score").mark_line(color="red", size=3)
        
        return apply_theme(scatter + line)
    

app = App(app_ui, server)