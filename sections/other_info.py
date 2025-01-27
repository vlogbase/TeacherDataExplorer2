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
    
    # Employment Type Distribution
    st.subheader("Employment Type Analysis")
    employment_dist = df['Employment Type'].value_counts()
    fig_employment = create_bar_chart(
        employment_dist.reset_index(),
        x='index',
        y='Employment Type',
        title='Distribution of Employment Types'
    )
    st.plotly_chart(fig_employment, use_container_width=True)
    
    # Marital Status Distribution
    st.subheader("Marital Status Distribution")
    marital_dist = df['Marital Status'].value_counts()
    fig_marital = create_bar_chart(
        marital_dist.reset_index(),
        x='index',
        y='Marital Status',
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
