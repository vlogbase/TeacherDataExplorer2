import streamlit as st
from utils.visualizations import create_bar_chart
import pandas as pd

def show(df):
    st.header("8. Other Information")

    # Additional Statistics
    st.subheader("Summary Statistics")

    col1, col2, col3 = st.columns(3)

    with col1:
        total_teachers = len(df)
        st.metric("Total Teachers", total_teachers)

    with col2:
        total_lgas = df['LGA'].nunique()
        st.metric("Total LGAs", total_lgas)

    with col3:
        total_subjects = df['Subjects Taught'].str.split(',').explode().nunique()
        st.metric("Unique Subjects", total_subjects)

    # Clean the data
    df_cleaned = df.copy()
    df_cleaned['Marital Status'] = df_cleaned['Marital Status'].replace('Marital Status', None)
    df_cleaned['Marital Status'] = df_cleaned['Marital Status'].fillna('Not Specified')
    df_cleaned['Employment Type'] = df_cleaned['Employment Type'].replace('Employment Type', None)
    df_cleaned['Employment Type'] = df_cleaned['Employment Type'].fillna('Not Specified')

    # Employment Type Distribution
    st.subheader("Employment Type Analysis")
    employment_dist = df_cleaned['Employment Type'].value_counts().reset_index()
    employment_dist.columns = ['Type', 'Count']
    fig_employment = create_bar_chart(
        employment_dist,
        x='Type',
        y='Count',
        title='Distribution of Employment Types'
    )
    st.plotly_chart(fig_employment, use_container_width=True)

    # Marital Status Distribution
    st.subheader("Marital Status Distribution")
    marital_dist = df_cleaned['Marital Status'].value_counts().reset_index()
    marital_dist.columns = ['Status', 'Count']
    fig_marital = create_bar_chart(
        marital_dist,
        x='Status',
        y='Count',
        title='Distribution of Marital Status'
    )
    st.plotly_chart(fig_marital, use_container_width=True)

    # Data Download Option
    st.subheader("Download Data")
    st.write("Download the complete dataset as CSV:")

    @st.cache_data
    def convert_df_to_csv(df):
        return df.to_csv(index=False).encode('utf-8')

    csv = convert_df_to_csv(df)
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name='nigerian_teachers_data.csv',
        mime='text/csv'
    )