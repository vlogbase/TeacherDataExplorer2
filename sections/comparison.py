import streamlit as st
from utils.visualizations import create_bar_chart, create_pie_chart, create_histogram

def show(df):
    st.header("Comparison Analysis")

    if 'selected_graphs' not in st.session_state:
        st.session_state.selected_graphs = []

    if not st.session_state.selected_graphs:
        st.info("No graphs selected for comparison. Use the 'Add to Compare' checkbox below any graph to add it here.")
        return

    # Display all selected graphs
    cols = st.columns(2)
    for idx, graph in enumerate(st.session_state.selected_graphs):
        with cols[idx % 2]:
            # Ensure full container width and proper spacing
            st.plotly_chart(graph['figure'], use_container_width=True)
            if st.button(f"Remove {graph['title']}", key=f"remove_{idx}"):
                st.session_state.selected_graphs.pop(idx)
                st.rerun()