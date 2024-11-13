import streamlit as st
from PIL import Image
from create_account_file import get_create_account_page
from custom_css_file import get_custom_css_page
from data_file import interests, activities

def get_profile_info_page():
    get_custom_css_page(alignment="left", button_span="auto")
    
    # Display the predefined interest options (from the imported variable)
    st.write(interests)
    
    # Format user's email prefix
    email_prefix = st.session_state.user_email.split('@')[0]
    formatted_prefix = f"{email_prefix[0].upper()}. {email_prefix[1:].capitalize()}"
    st.title(f"{formatted_prefix}'s Profile") 
    
    # Collect user's 1st-degree connections
    connections = st.text_input("Enter your friends (ie. AKotlan, RMiller, SLogan, etc.)")
    
    # Predefined options for interests and activities
    interest_options = interests
    activity_options = activities
    
    # Collect user's interests using a multi-select option without a default value
    selected_interests = st.multiselect("Select your interests", interest_options)
    
    # Collect user's activities using a multi-select option without a default value
    selected_activities = st.multiselect("Select your activities", activity_options)

    # Button to submit the profile information
    if st.button('Enter', use_container_width=False):
        st.session_state.page = "student_landing_page"
