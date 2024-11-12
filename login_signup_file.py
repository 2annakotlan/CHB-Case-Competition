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
                margin: 10px 0;  /* Vertical margin for spacing between buttons */
                width: 250px;    /* Set a fixed width for the buttons */
                height: 50px;    /* Set a fixed height for the buttons */
                border-radius: 25px; /* Rounded corners */
                border: none;  /* No borders */
                background-color: #4CAF50; /* Solid green background */
                color: white;  /* White text */
                font-size: 16px;
                font-weight: bold;
                cursor: pointer;
                transition: background-color 0.3s ease;  /* Smooth background change on hover */
            }
            .stButton:hover {
                background-color: #45a049; /* Slightly darker green on hover */
            }
        </style>
    """, unsafe_allow_html=True)

    # Create the buttons using Streamlit's built-in functionality
    st.markdown('<div class="center-buttons">', unsafe_allow_html=True)  # Center the buttons
    
    if st.button("Create Account"):
        st.write("Redirecting to create account page...")
    
    if st.button("Sign In"):
        st.write("Redirecting to sign-in page...")

    st.markdown('</div>', unsafe_allow_html=True)

