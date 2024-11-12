import streamlit as st

def get_login_signup_page():
    # Title and Slogan
    st.markdown("<h1 style='text-align: center;'>Welcome to My App</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Your ultimate solution for productivity</p>", unsafe_allow_html=True)

    # Apply background color to the entire page and style buttons
    st.markdown("""
        <style>
            body {
                background-color: #007BFF; /* Blue background */
                color: white; /* White text for the entire page */
                font-family: 'Arial', sans-serif; /* Clean font */
            }
            .center-buttons {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
            }
            .stButton {
                margin: 15px;
                width: 200px;
                height: 50px;
                border-radius: 25px; /* Rounded corners */
                border: none;  /* No borders */
                background-color: #4CAF50; /* Green background */
                color: white;  /* White text */
                font-size: 16px;
                font-weight: bold;
                cursor: pointer;
                transition: background-color 0.3s ease;  /* Smooth background change on hover */
            }
            .stButton:hover {
                background-color: #45a049; /* Darker green on hover */
            }
        </style>
        <div class="center-buttons">
            <button class="stButton">Create Account</button>
            <button class="stButton">Sign In</button>
        </div>
    """, unsafe_allow_html=True)
