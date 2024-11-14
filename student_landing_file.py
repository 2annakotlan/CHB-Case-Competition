import streamlit as st
from custom_css_file import get_custom_css_page

# Function to handle the student landing page view
def get_student_landing_page():
    get_custom_css_page(alignment="center", button_span="full")
    
    st.title("Student Dashboard")
    st.write("Welcome, student! This is your personal dashboard.")
    st.write("Explore resources, courses, and more.")
    
    # Create two columns for the clickable boxes
    col1, col2 = st.columns(2)

    # First clickable box
    with col1:
        if st.button("Box 1", key="box1"):
            st.session_state.page = "friend_swiping_page"
    
    # Second clickable box
    with col2:
        if st.button("Box 2", key="box2"):
            st.session_state.page = "activity_suggestions_page"
    
    # Optionally, add a button to go back to the login/signup page
    if st.button('Log out'):
        st.session_state.page = "login_signup_page"

    if st.button('Edit Profile'):
        st.session_state.page = "profile_info_page"
