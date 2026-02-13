from shiny import App, ui

app_ui = ui.page_fillable(
    ui.panel_title("Academic Performance Dashboard"),
    ui.layout_sidebar(
        ui.sidebar(
            ui.h4("Sidebar inputs"),
            ui.p("Placeholder for filters (e.g., grade range, subject, gender, lunch, test prep)."),
            open="desktop",
        ),
        ui.layout_columns(
            ui.value_box("Total students", "Placeholder"),
            ui.value_box("Average score", "Placeholder"),
            ui.value_box("Performance gap", "Placeholder"),
            fill=False,
        ),
        ui.layout_columns(
            ui.card(
                ui.card_header("Data preview"),
                ui.p("Placeholder for a data table (e.g., aggregated summary by group)."),
                full_screen=True,
            ),
            ui.card(
                ui.card_header("Main visualization"),
                ui.p("Placeholder for a chart (e.g., score distribution / group comparison)."),
                full_screen=True,
            ),
            col_widths=[6, 6],
        ),
        ui.layout_columns(
            ui.card(
                ui.card_header("Secondary visualization"),
                ui.p("Placeholder for an additional chart (e.g., trend / distribution / subgroup analysis)."),
                full_screen=True,
            )
        ),
    ),
)


def server(input, output, session):
    # Milestone 1: skeleton only (no server logic yet)
    pass


app = App(app_ui, server)