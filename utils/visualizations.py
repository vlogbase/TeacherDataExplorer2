import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import streamlit as st

def _add_to_comparison(fig, title):
    """Helper function to add a graph to comparison section."""
    if 'selected_graphs' not in st.session_state:
        st.session_state.selected_graphs = []

    # Check if graph is already in comparison
    if not any(g['title'] == title for g in st.session_state.selected_graphs):
        # Update figure layout for better display in comparison view
        fig.update_layout(
            height=500,  # Fixed height for consistency
            width=None,  # Allow width to be responsive
            margin=dict(t=50, l=50, r=50, b=50),
            showlegend=True,
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            )
        )
        st.session_state.selected_graphs.append({
            'figure': fig,
            'title': title
        })

def create_bar_chart(df, x, y, title, orientation='v', color=None, barmode=None):
    """Create a bar chart using Plotly."""
    # If x column contains numeric-like strings, convert and sort
    if isinstance(df[x].iloc[0], str) and any(c.isdigit() for c in df[x].iloc[0]):
        try:
            # Extract first number from string and convert to float
            df = df.copy()
            df[x] = pd.to_numeric(df[x].str.extract('(\d+)', expand=False))
            df = df.sort_values(by=x)
        except:
            pass

    fig = px.bar(
        df,
        x=x,
        y=y,
        title=title,
        orientation=orientation,
        color=color,
        barmode=barmode,
        template='plotly_white',
        height=400  # Default height for regular view
    )
    fig.update_layout(
        title_x=0.5,
        margin=dict(t=50, l=50, r=50, b=50)
    )

    # Add comparison checkbox
    if st.checkbox(f"Add to Compare", key=f"compare_{title}"):
        _add_to_comparison(fig, title)

    return fig

def create_pie_chart(df, names, values, title):
    """Create a pie chart using Plotly."""
    fig = px.pie(
        df,
        names=names,
        values=values,
        title=title,
        height=400  # Default height for regular view
    )
    fig.update_layout(
        title_x=0.5,
        margin=dict(t=50, l=50, r=50, b=50)
    )

    # Add comparison checkbox
    if st.checkbox(f"Add to Compare", key=f"compare_{title}"):
        _add_to_comparison(fig, title)

    return fig

def create_histogram(df, column, title):
    """Create a histogram using Plotly."""
    fig = px.histogram(
        df,
        x=column,
        title=title,
        template='plotly_white',
        height=400  # Default height for regular view
    )
    fig.update_layout(
        title_x=0.5,
        margin=dict(t=50, l=50, r=50, b=50)
    )

    # Add comparison checkbox
    if st.checkbox(f"Add to Compare", key=f"compare_{title}"):
        _add_to_comparison(fig, title)

    return fig

def create_scatter_plot(df, x, y, color, title):
    """Create a scatter plot using Plotly."""
    fig = px.scatter(
        df,
        x=x,
        y=y,
        color=color,
        title=title,
        template='plotly_white',
        height=400  # Default height for regular view
    )
    fig.update_layout(
        title_x=0.5,
        margin=dict(t=50, l=50, r=50, b=50)
    )

    # Add comparison checkbox
    if st.checkbox(f"Add to Compare", key=f"compare_{title}"):
        _add_to_comparison(fig, title)

    return fig