import streamlit as st

def get_login_signup_page():
    # Title and Slogan
    st.markdown("<h1 style='text-align: center;'>Better Together</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>building an interconnected community</p>", unsafe_allow_html=True)

    # Center the buttons using HTML and CSS
    st.markdown("""
        <style>
            .center-buttons {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
            }
            .stButton {
                margin: 10px;
            }
        </style>
        <div class="center-buttons">
            <button class="stButton" style="width: 200px;">Create Account</button>
            <button class="stButton" style="width: 200px;">Sign In</button>
        </div>
    """, unsafe_allow_html=True)
