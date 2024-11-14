import streamlit as st
from custom_css_file import get_custom_css_page

def get_create_account_page():
    get_custom_css_page(alignment="left", button_span="full")

    st.title("Create Your Account")
    st.write("Enter your Bentley University email and password to sign up")
    
    # Set default email and disable the input
    email = st.text_input("Email", value="akotlan@falcon.bentley.edu", disabled=True)
    
    password = st.text_input("Password", type="password")
    
    # Layout the buttons side by side using columns
    col1, col2 = st.columns([1, 1])
    
    with col1:
        back_clicked = st.button("Back")
    
    with col2:
        next_clicked = st.button("Next")
    
    if next_clicked:
        st.session_state.page = "profile_info_page"

    if back_clicked:
        st.session_state.page = "login_signup_page"
