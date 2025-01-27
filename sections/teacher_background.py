import streamlit as st
from utils.visualizations import create_bar_chart, create_histogram
import pandas as pd

def show(df):
    st.header("2. Teacher Background")
    
    # State of Origin Analysis
    st.subheader("State of Origin Distribution")
    state_dist = df['State of Origin'].value_counts()
    fig_state = create_bar_chart(
        state_dist.reset_index(),
        x='index',
        y='State of Origin',
        title='Distribution by State of Origin'
    )
    st.plotly_chart(fig_state, use_container_width=True)
    
    # State of Origin by Gender
    st.subheader("State of Origin by Gender")
    state_gender = pd.crosstab(df['State of Origin'], df['Gender'])
    fig_state_gender = create_bar_chart(
        state_gender.reset_index(),
        x='State of Origin',
        y=['Male', 'Female'],
        title='State of Origin Distribution by Gender'
    )
    st.plotly_chart(fig_state_gender, use_container_width=True)
    
    # Age Distribution
    st.subheader("Age Distribution")
    df['Age'] = pd.to_datetime(df['Date of Birth']).dt.year.apply(lambda x: 2024 - x)
    fig_age = create_histogram(
        df,
        'Age',
        'Age Distribution of Teachers'
    )
    st.plotly_chart(fig_age, use_container_width=True)
