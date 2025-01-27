import streamlit as st
from utils.visualizations import create_bar_chart, create_pie_chart
import pandas as pd

def show(df):
    st.header("3. Teacher Employment Information")
    
    # Academic vs Non-Academic Staff
    st.subheader("Employment Type Distribution")
    employment_dist = df['Employment Type'].value_counts()
    fig_employment = create_pie_chart(
        employment_dist.reset_index(),
        names='index',
        values='Employment Type',
        title='Distribution by Employment Type'
    )
    st.plotly_chart(fig_employment, use_container_width=True)
    
    # Grade Level Distribution
    st.subheader("Grade Level Distribution")
    grade_dist = df['Grade Level'].value_counts()
    fig_grade = create_bar_chart(
        grade_dist.reset_index(),
        x='index',
        y='Grade Level',
        title='Distribution by Grade Level'
    )
    st.plotly_chart(fig_grade, use_container_width=True)
    
    # Years in Current School
    st.subheader("Years in Current School")
    years_dist = df['Years in Current School'].value_counts()
    fig_years = create_bar_chart(
        years_dist.reset_index(),
        x='index',
        y='Years in Current School',
        title='Distribution by Years in Current School'
    )
    st.plotly_chart(fig_years, use_container_width=True)
