import streamlit as st

def get_login_signup_page(background_image_url):
    # Set the background image from the URL
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{background_image_url}");
            background-size: cover;
            background-position: center;
            height: 100vh;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Create the title and description
    st.title("Welcome to the App!")
    st.write("Please log in or sign up to continue.")

    # Create buttons for login and signup
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Login"):
            st.write("You clicked on Login!")
            # Add login logic here (e.g., input fields, authentication)
    with col2:
        if st.button("Sign Up"):
            st.write("You clicked on Sign Up!")
            # Add sign-up logic here (e.g., input fields, account creation)

