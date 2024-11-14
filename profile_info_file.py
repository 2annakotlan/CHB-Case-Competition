import streamlit as st
import pandas as pd
from create_account_file import get_create_account_page
from custom_css_file import get_custom_css_page
from activities_interests_data_file import interests, activities
from population_data_file import population_df  # Ensure this import is correct

def get_profile_info_page():
    # Apply custom CSS with specified alignment and button span
    get_custom_css_page(alignment="left", button_span="auto")

    st.write(population_df)
    
