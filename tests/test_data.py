import pytest
import pandas as pd
import ibis
from app import filter_student_data 

def toy_student_data():
    """
    Returns a small toy dataset with rows containing school_type, parental_education_level, exam_score, and
    hours_studied registered in a DuckDB connection
    """
    toy_df = pd.DataFrame({
        "School_Type": ["Public", "Private", "Public", "Private", "Public"],
        "Parental_Education_Level": ["High School", "College", "Postgraduate", "High School", "College"],
        "Exam_Score": [65, 85, 92, 70, 75],
        "Hours_Studied": [10, 20, 25, 12, 15]
    })
    con = ibis.duckdb.connect()
    con.register(toy_df, table_name="test_students")
    return con


def test_filter_school_type(toy_student_df):
    """Tests that filter_student_data filters correctly by school type."""
    
    result = filter_student_data(toy_student_df, school_types=["Private"])
    result_df = result.execute()

    assert len(result_df) == 2
    assert all(result_df["School_Type"] == "Private")


def test_filter_parent_edu(mock_student_table):
    """Tests that filter_student_data filters correctly by parental education level."""
    
    result = filter_student_data(mock_student_table, parent_edu_levels=["College"])
    result_df = result.execute()

    assert len(result_df) == 2
    assert all(result_df["Parental_Education_Level"] == "College")
