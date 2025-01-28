import streamlit as st
from utils.visualizations import create_bar_chart, create_pie_chart
import pandas as pd

def show(df):
    st.header("4. Previous Employment Experience")

    # Number of schools worked in over last 5 years
    st.subheader("Schools Worked in Last 5 Years")
    schools_count = df['Years in Current School'].value_counts().reset_index()
    schools_count.columns = ['Experience', 'Count']
    fig_schools = create_bar_chart(
        schools_count,
        x='Experience',
        y='Count',
        title='Distribution of Experience in Current School'
    )
    st.plotly_chart(fig_schools, use_container_width=True)

    # Reason for becoming a teacher
    st.subheader("Reason for Teaching")
    reason_dist = df['Reason for Teaching'].value_counts().reset_index()
    reason_dist.columns = ['Reason', 'Count']
    fig_reason = create_pie_chart(
        reason_dist,
        names='Reason',
        values='Count',
        title='Reasons for Becoming a Teacher'
    )
    st.plotly_chart(fig_reason, use_container_width=True)

    # Reason for teaching by gender
    st.subheader("Reason for Teaching by Gender")
    reason_gender = df.groupby(['Reason for Teaching', 'Gender']).size().reset_index(name='Count')
    fig_reason_gender = create_bar_chart(
        reason_gender,
        x='Reason for Teaching',
        y='Count',
        color='Gender',
        title='Teaching Motivation by Gender',
        barmode='group'
    )
    st.plotly_chart(fig_reason_gender, use_container_width=True)