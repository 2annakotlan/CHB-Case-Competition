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
    """, unsafe_allow_html=True)

    # Create the buttons using Streamlit's built-in functionality
    col1, col2 = st.columns(2)  # Create two columns for layout

    with col1:
        if st.button("Create Account"):
            # Action for "Create Account" button
            st.write("Redirecting to create account page...")

    with col2:
        if st.button("Sign In"):
            # Action for "Sign In" button
            st.write("Redirecting to sign-in page...")

