# IMPORT PACKAGES AND OBJECTS 
from data_file import friend_swiping_df
from friend_swiping_file import get_friend_swiping_page
from login_signup_file import get_login_signup_page

import streamlit as st

# Custom CSS to set a medium blue background
st.markdown(
    """
    <style>
    body {
        background-color: #4682B4;  /* Medium Blue */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Your Streamlit app content
st.title('My Streamlit App with a Medium Blue Background')
st.write("Welcome to my Streamlit app with a customized background color!")
