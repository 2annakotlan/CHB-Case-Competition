import streamlit as st
from custom_css_file import get_custom_css_page

# Function to handle the sign-in page
def get_sign_in_page():
    get_custom_css_page(alignment="left")
    
    st.title("Sign In")
    st.write("Enter your Bentley University email and password to sign in")
    
    # Collect user inputs for email and password
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    
    # Handle button click event
    if st.button("Sign In"):
        # Check if the email ends with @falcon.bentley.edu and contains only one @ symbol
        if not email.endswith("@falcon.bentley.edu") or email.count('@') != 1:
            st.error("Please enter a valid Bentley University email address")
        elif email == "admin@falcon.bentley.edu":  # Check if the email is admin
            st.session_state.page = "admin_landing_page"  # Go to admin landing page
            st.success("You are signed in successfully as Admin!")
        else:
            st.session_state.page = "student_landing_page"  # Go to student landing page
            st.success("You are signed in successfully as a Student!")
