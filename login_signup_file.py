import streamlit as st

def get_login_signup_page():
    # Title and Slogan
    st.markdown("<h1 style='text-align: center;'>Welcome to My App</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Your ultimate solution for productivity</p>", unsafe_allow_html=True)

    # Apply background color to the page and style buttons
    st.markdown("""
        <style>
            html, body {
                background-color: #007BFF;
                color: white;
                font-family: 'Arial', sans-serif;
                height: 100%;
                margin: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                flex-direction: column;
            }
            .stButton {
                margin: 15px;
                width: 200px;
                height: 50px;
                border-radius: 25px;
                border: none;
                background-color: #4CAF50;
                color: white;
                font-size: 16px;
                font-weight: bold;
                cursor: pointer;
                transition: background-color 0.3s ease;
            }
            .stButton:hover {
                background-color: #45a049;
            }
        </style>
        <button class="stButton">Create Account</button>
        <button class="stButton">Sign In</button>
    """, unsafe_allow_html=True)
