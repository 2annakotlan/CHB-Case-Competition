from custom_css_file import get_custom_css_page
import streamlit as st

# Function for the login/signup page content
def get_login_signup_page():
    get_custom_css_page(alignment="center")

    # Center the title and subtitle
    st.markdown("<h1>Better Together</h1>", unsafe_allow_html=True)
    st.markdown("<p>Building an interconnected community</p>", unsafe_allow_html=True)

    # Add spacing before buttons
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Create buttons stacked vertically
    if st.button('Create Account', use_container_width=True):
        st.session_state.page = "create_account_page"

    st.markdown("<br>", unsafe_allow_html=True)  # Add space between buttons

    if st.button('Sign In', use_container_width=True):
        st.session_state.page = "sign_in_page"
