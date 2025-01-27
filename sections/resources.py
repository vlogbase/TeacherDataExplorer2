import streamlit as st
from utils.visualizations import create_bar_chart, create_pie_chart
import pandas as pd

def show(df):
    st.header("7. School Resources and Academic Materials")
    
    # Sufficient Resources Analysis
    st.subheader("Resource Sufficiency")
    resource_dist = df['Sufficient Resources'].value_counts()
    fig_resources = create_pie_chart(
        resource_dist.reset_index(),
        names='index',
        values='Sufficient Resources',
        title='Distribution of Resource Sufficiency'
    )
    st.plotly_chart(fig_resources, use_container_width=True)
    
    # Resource Priorities
    st.subheader("Resource Priorities")
    # Split and clean resource priorities
    priorities = df['Resource Priorities'].str.split(',').explode().str.strip()
    priority_dist = priorities.value_counts()
    fig_priorities = create_bar_chart(
        priority_dist.reset_index(),
        x='index',
        y='Resource Priorities',
        title='Distribution of Resource Priorities'
    )
    st.plotly_chart(fig_priorities, use_container_width=True)
    
    # Resource Sufficiency by LGA
    st.subheader("Resource Sufficiency by LGA")
    resource_lga = pd.crosstab(df['LGA'], df['Sufficient Resources'])
    fig_resource_lga = create_bar_chart(
        resource_lga.reset_index(),
        x='LGA',
        y=['Yes', 'No'],
        title='Resource Sufficiency by LGA'
    )
    st.plotly_chart(fig_resource_lga, use_container_width=True)
