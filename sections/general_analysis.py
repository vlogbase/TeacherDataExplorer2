import streamlit as st
from utils.visualizations import create_bar_chart, create_pie_chart
import pandas as pd

def show(df):
    st.header("1. General Analysis")

    # Question 2: Number of teachers who responded
    st.subheader("Total Number of Respondents")
    total_teachers = len(df)
    st.metric("Total Teachers", total_teachers)

    # Question 3: Gender distribution
    st.subheader("Gender Distribution")
    gender_dist = df['Gender'].value_counts().reset_index()
    gender_dist.columns = ['Gender', 'Count']
    fig_gender = create_pie_chart(
        gender_dist,
        names='Gender',
        values='Count',
        title='Distribution by Gender'
    )
    st.plotly_chart(fig_gender, use_container_width=True)

    # Question 4: LGA distribution
    st.subheader("Distribution by LGA")
    lga_dist = df['LGA'].value_counts().reset_index()
    lga_dist.columns = ['LGA', 'Count']
    fig_lga = create_bar_chart(
        lga_dist,
        x='LGA',
        y='Count',
        title='Number of Teachers by LGA'
    )
    st.plotly_chart(fig_lga, use_container_width=True)

    # Question 5: Gender distribution by LGA
    st.subheader("Gender Distribution by LGA")
    # Melt the crosstab to create a long-format dataframe suitable for plotting
    gender_lga_data = pd.crosstab(df['LGA'], df['Gender']).reset_index()
    gender_lga_melted = pd.melt(
        gender_lga_data,
        id_vars=['LGA'],
        value_vars=['Male', 'Female'],
        var_name='Gender',
        value_name='Count'
    )
    fig_gender_lga = create_bar_chart(
        gender_lga_melted,
        x='LGA',
        y='Count',
        color='Gender',
        title='Gender Distribution by LGA',
        barmode='group'
    )
    st.plotly_chart(fig_gender_lga, use_container_width=True)