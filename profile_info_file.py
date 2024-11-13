import streamlit as st
from PIL import Image
from create_account_file import get_create_account_page

def get_profile_info_page():
    email_prefix = st.session_state.user_email.split('@')[0]
    formatted_prefix = f"{email_prefix[0].upper()}. {email_prefix[1:].capitalize()}"
    st.title(f"{formatted_prefix}'s Profile") 
    
    # Collect user's 1st-degree connections (still a text input)
    connections = st.text_input("Enter your friends (ie. AKotlan, RMiller, SLogan, etc.))", )
    
    # Predefined options for interests and activities
    interest_options = ["Coding", "Music", "Hiking", "Reading", "Sports", "Traveling"]
    activity_options = ["Gym", "Running", "Yoga", "Painting", "Photography", "Cooking"]
    
    # Collect user's interests using a multi-select option without a default value
    interests = st.multiselect("Select your interests", interest_options)
    
    # Collect user's activities using a multi-select option without a default value
    activities = st.multiselect("Select your activities", activity_options)
    
