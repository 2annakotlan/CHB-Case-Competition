from custom_css_file import get_custom_css_page
import streamlit as st
from activities_interests_data_file import activities, interests
import pandas as pd

def get_profile_info_page():
    # Apply custom CSS with specified alignment and button span
    get_custom_css_page(alignment="left", button_span="auto") 

    # Format user's email prefix for the profile title
    st.title("Liam's Profile")
    
    # Collect user's 1st-degree connections
    selected_connections = st.text_input("Enter your friends", value="Kelley, Noah, Jack", disabled=True)

    # Predefined options for interests and activities from imported data files
    interest_options = interests
    activity_options = activities

    # Collect user's interests using a multi-select option without a default value
    selected_interests = st.multiselect("Select your interests", interest_options, default=["STEM", "Games", "Performing Arts"], disabled=True)

    # Collect user's activities using a multi-select option without a default value
    selected_activities = st.multiselect("Select your activities", activity_options, default=["DECA", "Tamid", "Cheer"], disabled=True)
    
    # Button to submit the profile information
    if st.button('Enter', use_container_width=False):
        st.session_state.page = "student_landing_page"
