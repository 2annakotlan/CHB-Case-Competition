import streamlit as st

# Function to initialize the page state if not already set
def get_initialize_page():
    if 'page' not in st.session_state:
        st.session_state.page = 'login_signup_page'  # Default starting page