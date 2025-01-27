import plotly.express as px
import plotly.graph_objects as go

def create_bar_chart(df, x, y, title, orientation='v'):
    """Create a bar chart using Plotly."""
    fig = px.bar(
        df,
        x=x,
        y=y,
        title=title,
        orientation=orientation,
        template='plotly_white'
    )
    fig.update_layout(
        title_x=0.5,
        margin=dict(t=50, l=50, r=50, b=50)
    )
    return fig

def create_pie_chart(df, names, values, title):
    """Create a pie chart using Plotly."""
    fig = px.pie(
        df,
        names=names,
        values=values,
        title=title
    )
    fig.update_layout(
        title_x=0.5,
        margin=dict(t=50, l=50, r=50, b=50)
    )
    return fig

def create_histogram(df, column, title):
    """Create a histogram using Plotly."""
    fig = px.histogram(
        df,
        x=column,
        title=title,
        template='plotly_white'
    )
    fig.update_layout(
        title_x=0.5,
        margin=dict(t=50, l=50, r=50, b=50)
    )
    return fig

def create_scatter_plot(df, x, y, color, title):
    """Create a scatter plot using Plotly."""
    fig = px.scatter(
        df,
        x=x,
        y=y,
        color=color,
        title=title,
        template='plotly_white'
    )
    fig.update_layout(
        title_x=0.5,
        margin=dict(t=50, l=50, r=50, b=50)
    )
    return fig
