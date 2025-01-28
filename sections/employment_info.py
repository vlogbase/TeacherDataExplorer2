import streamlit as st
from utils.visualizations import create_bar_chart, create_pie_chart
import pandas as pd

def show(df):
    st.header("3. Teacher Employment Information")

    # Academic vs Non-Academic Staff
    st.subheader("Employment Type Distribution")
    employment_dist = df['Employment Type'].value_counts().reset_index()
    employment_dist.columns = ['Employment Type', 'Count']
    fig_employment = create_pie_chart(
        employment_dist,
        names='Employment Type',
        values='Count',
        title='Distribution by Employment Type'
    )
    st.plotly_chart(fig_employment, use_container_width=True)

    # Grade Level Distribution
    st.subheader("Grade Level Distribution")
    grade_dist = df['Grade Level'].value_counts().reset_index()
    grade_dist.columns = ['Grade Level', 'Count']
    fig_grade = create_bar_chart(
        grade_dist,
        x='Grade Level',
        y='Count',
        title='Distribution by Grade Level'
    )
    st.plotly_chart(fig_grade, use_container_width=True)

    # Years in Current School
    st.subheader("Years in Current School")
    # Clean and convert years data to numeric format
    df['Years in Current School'] = pd.to_numeric(
        df['Years in Current School'].astype(str).str.extract('(\d+)', expand=False),
        errors='coerce'
    )
    years_dist = df['Years in Current School'].value_counts().reset_index()
    years_dist.columns = ['Years', 'Count']
    years_dist = years_dist.sort_values('Years')  # Sort by years in ascending order
    fig_years = create_bar_chart(
        years_dist,
        x='Years',
        y='Count',
        title='Distribution by Years in Current School'
    )
    st.plotly_chart(fig_years, use_container_width=True)