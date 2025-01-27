import streamlit as st
import pandas as pd
from utils.data_processor import load_and_process_data
from sections import (
    general_analysis, teacher_background, employment_info,
    previous_experience, qualifications, role_info,
    resources, other_info
)

st.set_page_config(
    page_title="Nigerian Teachers Analysis",
    page_icon="📊",
    layout="wide"
)

def main():
    st.title("Nigerian Teachers Data Analysis Dashboard")

    # Load data
    df = load_and_process_data("attached_assets/merged_teachers_data.csv")

    # Sidebar navigation
    st.sidebar.title("Navigation")
    section = st.sidebar.radio(
        "Select Analysis Section",
        ["General Analysis", "Teacher Background", "Employment Information",
         "Previous Experience", "Qualifications", "Role Information",
         "School Resources", "Other Information"]
    )

    # Display selected section
    if section == "General Analysis":
        general_analysis.show(df)
    elif section == "Teacher Background":
        teacher_background.show(df)
    elif section == "Employment Information":
        employment_info.show(df)
    elif section == "Previous Experience":
        previous_experience.show(df)
    elif section == "Qualifications":
        qualifications.show(df)
    elif section == "Role Information":
        role_info.show(df)
    elif section == "School Resources":
        resources.show(df)
    else:
        other_info.show(df)

if __name__ == "__main__":
    main()