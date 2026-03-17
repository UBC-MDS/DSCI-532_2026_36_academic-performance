from shiny.playwright import controller
from shiny.run import ShinyAppProc
from shiny.pytest import create_app_fixture
from playwright.sync_api import Page

# Ensure this path points correctly to your app.py from inside the tests/ folder
app = create_app_fixture("../src/app.py")

def test_initial_dashboard_state(page, app) -> None:
    """Tests that the initial dashboard loads with all filters selected and starting metrics."""
    page.goto(app.url)
    page.wait_for_load_state("networkidle")

    school_type_cb = controller.InputCheckboxGroup(page, "school_type")
    
    # Verify the global filter starts with all options checked
    school_type_cb.expect_selected(["Public", "Private"])
    
    # Verify that the average exam score loads correctly
    avg_score_box = controller.OutputText(page, "avg_score")
    avg_score_box.expect_value("67.2%") 


def test_filtering_updates_metrics(page, app) -> None:
    """Tests that changing a filter correctly updates the average exam score output."""
    page.goto(app.url)
    page.wait_for_load_state("networkidle")

    school_type_cb = controller.InputCheckboxGroup(page, "school_type")
    avg_score_box = controller.OutputText(page, "avg_score")
    
    # Change the filter to show only private schools
    school_type_cb.set(["Private"])
    school_type_cb.expect_selected(["Private"])
    
    # Verify the metric changed 
    avg_score_box.expect_value("67.3%")


def test_empty_state_boundary(page, app) -> None:
    """Tests the boundary condition where no filters are selected, ensuring that the dashboard displays 'N/A'."""
    page.goto(app.url)
    page.wait_for_load_state("networkidle")

    school_type_cb = controller.InputCheckboxGroup(page, "school_type")
    avg_score_box = controller.OutputText(page, "avg_score")
    avg_hours_box = controller.OutputText(page, "avg_hours")
    avg_attendance_box = controller.OutputText(page, "avg_attendance")

    # Clear all selections to simulate an empty dataset boundary
    school_type_cb.set([])
    
    # Verify that the checkboxes are actually empty
    school_type_cb.expect_selected([])

    # Verify that the app handles the empty data by outputting "N/A" as programmed
    avg_score_box.expect_value("N/A")
    avg_hours_box.expect_value("N/A")
    avg_attendance_box.expect_value("N/A")
