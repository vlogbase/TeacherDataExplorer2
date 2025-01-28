import streamlit as st
from utils.visualizations import create_bar_chart, create_pie_chart
import pandas as pd

def show(df):
    st.header("5. Qualification Information")

    # Clean the qualification data
    df_cleaned = df.copy()
    df_cleaned['Teaching Qualification'] = df_cleaned['Teaching Qualification'].replace('Teaching Qualification', None)
    df_cleaned['Teaching Qualification'] = df_cleaned['Teaching Qualification'].fillna('Not Specified')

    df_cleaned['Highest Academic Qualification'] = df_cleaned['Highest Academic Qualification'].replace('Highest Academic Qualification', None)
    df_cleaned['Highest Academic Qualification'] = df_cleaned['Highest Academic Qualification'].fillna('Not Specified')

    # Teaching Qualification Distribution
    st.subheader("Teaching Qualifications")
    qual_dist = df_cleaned['Teaching Qualification'].value_counts().reset_index()
    qual_dist.columns = ['Qualification', 'Count']
    fig_qual = create_pie_chart(
        qual_dist,
        names='Qualification',
        values='Count',
        title='Distribution of Teaching Qualifications'
    )
    st.plotly_chart(fig_qual, use_container_width=True)

    # Highest Academic Qualification
    st.subheader("Highest Academic Qualification")
    academic_dist = df_cleaned['Highest Academic Qualification'].value_counts().reset_index()
    academic_dist.columns = ['Qualification', 'Count']
    fig_academic = create_bar_chart(
        academic_dist,
        x='Qualification',
        y='Count',
        title='Distribution of Highest Academic Qualifications'
    )
    st.plotly_chart(fig_academic, use_container_width=True)

    # Teaching Qualification by Gender
    st.subheader("Teaching Qualification by Gender")
    qual_gender = df_cleaned.groupby(['Teaching Qualification', 'Gender']).size().reset_index(name='Count')
    fig_qual_gender = create_bar_chart(
        qual_gender,
        x='Teaching Qualification',
        y='Count',
        color='Gender',
        title='Teaching Qualifications by Gender',
        barmode='group'
    )
    st.plotly_chart(fig_qual_gender, use_container_width=True)

    # TRCN Registration Status
    st.subheader("TRCN Registration Status")
    trcn_status = df_cleaned['TRCN'].notna().value_counts().reset_index()
    trcn_status.columns = ['Status', 'Count']
    fig_trcn = create_pie_chart(
        trcn_status,
        names='Status',
        values='Count',
        title='TRCN Registration Distribution'
    )
    st.plotly_chart(fig_trcn, use_container_width=True)