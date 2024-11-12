import streamlit as st
from custom_css_file import get_custom_css_page

# Function to handle the create account page
def get_create_account_page():
    get_custom_css_page(alignment="left")

    st.title("Create Your Account")
    st.write("Enter your Bentley University email and password to sign up")

    # Get the email input from the user
    email_input = st.text_input("Email", key="email")

    # Append the domain to the email if it's not already included
    if email_input and not email_input.endswith('@falcon.bentley.edu'):
        email = email_input + '@falcon.bentley.edu'
    else:
        email = email_input

    # Password input
    password = st.text_input("Password", type="password")

    # Submit button action
    if st.button("Submit"):
        if email == "admin@falcon.bentley.edu":  # Check if the email is admin
            st.session_state.page = "admin_landing_page"  # Go to admin landing page
        else:
            st.session_state.page = "student_landing_page"  # Go to student landing page
        st.success("Account created successfully!")
