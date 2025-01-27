import streamlit as st
from utils.visualizations import create_bar_chart, create_pie_chart
import pandas as pd

def show(df):
    st.header("5. Qualification Information")

    # Teaching Qualification Distribution
    st.subheader("Teaching Qualifications")
    qual_dist = df['Teaching Qualification'].value_counts().reset_index()
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
    academic_dist = df['Highest Academic Qualification'].value_counts().reset_index()
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
    qual_gender = pd.crosstab(df['Teaching Qualification'], df['Gender']).reset_index()
    fig_qual_gender = create_bar_chart(
        qual_gender,
        x='Teaching Qualification',
        y=['Male', 'Female'],
        title='Teaching Qualifications by Gender'
    )
    st.plotly_chart(fig_qual_gender, use_container_width=True)

    # TRCN Registration
    st.subheader("TRCN Registration Status")
    trcn_status = df['TRCN'].notna().value_counts().reset_index()
    trcn_status.columns = ['Status', 'Count']
    fig_trcn = create_pie_chart(
        trcn_status,
        names='Status',
        values='Count',
        title='TRCN Registration Distribution'
    )
    st.plotly_chart(fig_trcn, use_container_width=True)