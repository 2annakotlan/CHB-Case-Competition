import streamlit as st

def get_login_signup_page():
    # Title and Slogan
    st.markdown("<h1 style='text-align: center;'>Better Together</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>building an interconnected community</p>", unsafe_allow_html=True)

    # Center the buttons using layout containers (st.columns)
    st.markdown("""
        <style>
            .stButton {
                width: 250px;    /* Set a fixed width for the buttons */
                height: 50px;    /* Set a fixed height for the buttons */
                border-radius: 25px; /* Rounded corners */
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

    # Create two columns to center buttons vertically
    col1, col2 = st.columns([1, 1])  # Creating columns with equal width

    # Center buttons inside the columns
    with col1:
        st.empty()  # Empty space to center vertically

    with col2:
        if st.button("Create Account"):
            st.write("Redirecting to create account page...")

    with col1:
        st.empty()  # Empty space to center vertically

    with col2:
        if st.button("Sign In"):
            st.write("Redirecting to sign-in page...")

