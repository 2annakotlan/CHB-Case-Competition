import streamlit as st
from custom_css_file import get_custom_css_page

# Function to handle the sign-in page
def get_sign_in_page():
    get_custom_css_page(alignment="left")
    st.title("Sign In")
    st.write("Enter your email and password to sign in")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Sign In"):
        if email == "admin@falcon.bentley.edu":  # Check if the email is admin
            st.session_state.page = "admin_landing_page"  # Go to admin landing page
        else:
            st.session_state.page = "student_landing_page"  # Go to student landing page
        st.success("You are signed in successfully!")
