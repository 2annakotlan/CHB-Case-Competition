import streamlit as st
from custom_css_file import get_custom_css_page
from algorithm import network_map()

# Function to handle the admin landing page view
def get_admin_landing_page():
    get_custom_css_page(alignment="center", button_span="auto")
    
    st.title("Admin Dashboard")
    st.write("Welcome to the admin panel!")
    st.write("Here you can manage users, monitor activity, etc.")
    
    # Optionally, add a button to go back to the login/signup page
    if st.button('Log out'):
        st.session_state.page = "login_signup_page"

