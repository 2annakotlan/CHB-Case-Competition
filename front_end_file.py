# IMPORT PACKAGES AND OBJECTS 
from data_file import friend_swiping_df
from friend_swiping_file import get_friend_swiping_page
from login_signup_file import get_login_signup_page

import streamlit as st

def get_started_page():
    if st.session_state.page == 'login_signup':
        # Login/Signup Page
        st.title("Better Together")
        st.write("Building an interconnected community")

        # Buttons for navigating to the next pages
        if st.button('Create account'):
            st.session_state.page = "create_account"
        
        if st.button('Sign in'):
            st.session_state.page = "sign_in"

    elif st.session_state.page == 'create_account':
        # Create Account Page
        st.title("Create Your Account")
        st.write("Enter your email and choose a password")

        # Example of form input for account creation
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.button("Submit"):
            # You can add logic to create an account here
            st.session_state.page = "login_signup"  # Redirect back to the login/signup page
            st.success("Account created successfully!")

    elif st.session_state.page == 'sign_in':
        # Sign In Page
        st.title("Sign In")
        st.write("Enter your email and password to sign in")

        # Example of form input for sign-in
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.button("Sign In"):
            # You can add logic to authenticate the user here
            st.session_state.page = "login_signup"  # Redirect back to the login/signup page
            st.success("You are signed in successfully!")

get_started_page()
