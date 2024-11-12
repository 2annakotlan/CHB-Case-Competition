import streamlit as st

def get_login_signup_page():
   st.markdown("<h1 style='text-align: center;'>Welcome to My App</h1>", unsafe_allow_html=True)
   st.markdown("<p style='text-align: center;'>Your ultimate solution for productivity</p>", unsafe_allow_html=True)
   # Buttons for creating an account and signing in
   st.button("Create Account", key="create_account")
   st.button("Sign In", key="sign_in")
