from custom_css_file import get_custom_css_page
from nth_degree_file import get_full_df
import streamlit as st
from population_data_file import population_df
import pandas as pd

def get_activities_recommender_page():
    get_custom_css_page(alignment="center", button_span="full")

    # Retrieve population_df from session state
    population_df = st.session_state.get('population_df', pd.DataFrame())  # Default to empty DataFrame if not found

    # Display the updated DataFrame
    st.dataframe(population_df)


  
