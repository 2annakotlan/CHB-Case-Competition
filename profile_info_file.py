import streamlit as st
from PIL import Image
from create_account_file import get_create_account_page

def get_profile_info_page():
    email_prefix = st.session_state.user_email.split('@')[0]
    st.title(f"{email_prefix}'s Profile") 

    # Collect user's 1st-degree connections
    one_degree_connections = st.text_input("What are your 1st-degree connections?", "John, Sarah, Mike")

    # Collect user's interests
    interests = st.text_input("What are your interests?", "Coding, Music, Hiking")

    # Collect user's activities
    activities = st.text_input("What are your activities?", "Coding, Music, Hiking")
