import pandas as pd
import altair as alt
import ibis
from shiny import App, ui, render, reactive
from shinywidgets import output_widget, render_widget
from pathlib import Path
from querychat import QueryChat
import chatlas as clt
from dotenv import load_dotenv
import os

load_dotenv()

alt.data_transformers.disable_max_rows()

APP_DIR = Path(__file__).resolve().parent
PARQUET_PATH = APP_DIR.parent / "data" / "processed" / "StudentPerformanceFactors.parquet"

con = ibis.duckdb.connect()
t = con.read_parquet(PARQUET_PATH)

income_order = ["Low", "Medium", "High"]
involvement_order = ["Low", "Medium", "High"]

chat = clt.ChatGithub(model="gpt-4o")
qc = QueryChat(
    t.execute(), 
    "performance_data",
    client=chat,
    greeting=(
        "Hello! I can help you explore the Academic Performance dataset. "
        "Try asking things like:\n"
        "- *Show only public school students with an average exam score above 80%*\n"
        "- *Filter to students whose parents have a postgraduate education*\n"
        "- *Which school type has the highest average hours studied?*"
    ),
)

app_ui = ui.page_fluid(
    ui.panel_title("Academic Performance Dashboard"),
    ui.navset_tab(
        ui.nav_panel(
            "Dashboard",
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
                        choices=sorted(t.Parental_Education_Level.execute().unique().tolist()),
                        selected=sorted(t.Parental_Education_Level.execute().unique().tolist()),
                    ),
                    ui.hr(),
                    ui.markdown("**Authors:** Group Project | **DSCI 532**"),
                    open="desktop",
                ),
                ui.layout_columns(
                    ui.value_box("AVG Exam Score", ui.output_text("avg_score"), theme="primary"),
                    ui.value_box("AVG Hours Studied", ui.output_text("avg_hours")),
                    ui.value_box("AVG Attendance", ui.output_text("avg_attendance")),
                    fill=False,
                ),
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
        ),
        ui.nav_panel(
            "AI Assistant",
            ui.layout_sidebar(
                ui.sidebar(
                    qc.ui(),
                    width = 400
                ),
                ui.card(
                    ui.card_header("Filtered Data"),
                    ui.output_data_frame("ai_data_table"),
                    ui.download_button("download_ai_output",
                                      "Download dataframe as CSV"),
                    full_screen = True
                ),
            ),
        ),
    ),
)


def server(input, output, session):
    outputs = qc.server()

    @reactive.calc
    def filtered_query():
        query = t
        if input.school_type():
            query = query.filter(t.School_Type.isin(input.school_type()))
        if input.parent_edu():
            query = query.filter(t.Parental_Education_Level.isin(input.parent_edu()))
        
        return query

    @render.text
    def avg_score():
        q = filtered_query()
        val = q.Exam_Score.mean().to_pandas()
        return f"{val:.1f}%" if pd.notnull(val) else "N/A"

    @render.text
    def avg_hours():
        q = filtered_query()
        val = q.Hours_Studied.mean().to_pandas()
        return f"{val:.1f} hrs" if pd.notnull(val) else "N/A"

    @render.text
    def avg_attendance():
        q = filtered_query()
        val = q.Attendance.mean().to_pandas()
        return f"{val:.1f}%" if pd.notnull(val) else "N/A"

    def apply_theme(chart):
        return (
            chart.properties(width="container")
            .configure_axis(labelFontSize=14, titleFontSize=16)
            .configure_view(strokeWidth=0)
        )

    @render_widget
    def scatter_plot():
        data = filtered_query().select("Hours_Studied", "Exam_Score").execute()
        if data.empty:
            return alt.Chart(pd.DataFrame()).mark_text()

        plot_df = data.dropna()
        base = alt.Chart(plot_df).encode(
            x=alt.X("Hours_Studied:Q", title="Hours Studied"),
            y=alt.Y("Exam_Score:Q", title="Exam Score", scale=alt.Scale(domain=[40, 100])),
        )
        scatter = base.mark_circle(opacity=0.4, color="#21918c")
        line = base.transform_loess("Hours_Studied", "Exam_Score").mark_line(color="red", size=3)
        return apply_theme(scatter + line)

    @render_widget
    def income_boxplot():
        data = filtered_query().select("Family_Income", "Exam_Score").execute()
        if data.empty:
            return alt.Chart(pd.DataFrame()).mark_text()

        plot_df = data.dropna()
        chart = alt.Chart(plot_df).mark_boxplot(
            extent="min-max", size=60, clip=True
        ).encode(
            x=alt.X("Family_Income:N", sort=income_order, title="Family Income", axis=alt.Axis(labelAngle=0)),
            y=alt.Y("Exam_Score:Q", title="Exam Score", scale=alt.Scale(domain=[55, 80])),
            color=alt.Color("Family_Income:N", scale=alt.Scale(scheme="viridis"), legend=None),
        )
        return apply_theme(chart)

    @render_widget
    def involvement_bar():
        data = filtered_query().select("Parental_Involvement", "Exam_Score").execute()
        if data.empty:
            return alt.Chart(pd.DataFrame()).mark_text()

        plot_df = data.dropna()
        chart = alt.Chart(plot_df).mark_bar(size=80).encode(
            x=alt.X("Parental_Involvement:N", sort=involvement_order, title="Involvement Level", axis=alt.Axis(labelAngle=0)),
            y=alt.Y("mean(Exam_Score):Q", title="Average Exam Score", scale=alt.Scale(domain=[60, 72])),
            color=alt.Color("Parental_Involvement:N", scale=alt.Scale(scheme="viridis"), legend=None),
        )
        return apply_theme(chart)

    @render_widget
    def attendance_scatter():
        data = filtered_query().select("Attendance", "Exam_Score").execute()
        if data.empty:
            return alt.Chart(pd.DataFrame()).mark_text()

        plot_df = data.dropna()
        base = alt.Chart(plot_df).encode(
            x=alt.X("Attendance:Q", title="Attendance (%)", scale=alt.Scale(domain=[60, 100])),
            y=alt.Y("Exam_Score:Q", title="Exam Score", scale=alt.Scale(domain=[40, 100])),
        )
        scatter = base.mark_circle(opacity=0.4, color="#21918c")
        line = base.transform_loess("Attendance", "Exam_Score").mark_line(color="red", size=3)
        return apply_theme(scatter + line)

    @render.data_frame
    def ai_data_table():
        return outputs.df()

    @render.download
    def download_ai_output():
        yield outputs.df().to_csv(index = False)

app = App(app_ui, server)