import streamlit as st
from custom_css_file import get_custom_css_page

# Function to handle the student landing page view
def get_student_landing_page():
    get_custom_css_page(alignment="center", button_span="full")
    
    st.title("Student Dashboard")
    st.write("Welcome, student! This is your personal dashboard.")
    st.write("Explore resources, courses, and more.")
    
    image_url_1 = "https://raw.githubusercontent.com/2annakotlan/CHB-Case-Competition/main/swipe.png"
    image_url_2 = "https://raw.githubusercontent.com/2annakotlan/CHB-Case-Competition/main/house.png"

    col1, col2 = st.columns(2)

    with col1:
        st.image(image_url_1, use_column_width=True)

    with col2:
        st.image(image_url_2, use_column_width=True)
    
    # Optionally, add a button to go back to the login/signup page
    if st.button('Log out'):
        st.session_state.page = "login_signup_page"

    if st.button('Edit Profile'):
        st.session_state.page = "profile_info_page"
