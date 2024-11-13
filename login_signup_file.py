from custom_css_file import get_custom_css_page
import streamlit as st

# Function for the login/signup page content
def get_login_signup_page():
    get_custom_css_page(alignment="center", button_span="full")

    # Center the title and subtitle
    st.markdown("<h1>Better Together</h1>", unsafe_allow_html=True)
    st.markdown("<p>Building an interconnected community</p>", unsafe_allow_html=True)

    # Add spacing and create two-column layout for buttons
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button('Create Account', use_container_width=True):
            st.session_state.page = "create_account_page"
    
    with col2:
        if st.button('Sign In', use_container_width=True):
            st.session_state.page = "sign_in_page"

