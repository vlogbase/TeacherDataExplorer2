import streamlit as st
from utils.visualizations import create_bar_chart, create_pie_chart
import pandas as pd

def show(df):
    st.header("6. Teacher Role Information")

    # Job Title Distribution
    st.subheader("Job Titles")
    title_dist = df['Job Title'].value_counts().reset_index()
    title_dist.columns = ['Title', 'Count']
    fig_title = create_bar_chart(
        title_dist,
        x='Title',
        y='Count',
        title='Distribution of Job Titles'
    )
    st.plotly_chart(fig_title, use_container_width=True)

    # Subjects Taught
    st.subheader("Subjects Taught")
    # Split the subjects and count occurrences
    subjects = df['Subjects Taught'].str.split(',').explode().str.strip()
    subject_dist = subjects.value_counts().reset_index()
    subject_dist.columns = ['Subject', 'Count']
    fig_subjects = create_bar_chart(
        subject_dist,
        x='Subject',
        y='Count',
        title='Distribution of Subjects Taught'
    )
    st.plotly_chart(fig_subjects, use_container_width=True)

    # Subjects by Gender
    st.subheader("Subjects Taught by Gender")
    subjects_gender = pd.crosstab(subjects, df['Gender'].loc[subjects.index]).reset_index()
    fig_subjects_gender = create_bar_chart(
        subjects_gender,
        x='row_0',
        y=['Male', 'Female'],
        title='Subject Distribution by Gender'
    )
    st.plotly_chart(fig_subjects_gender, use_container_width=True)