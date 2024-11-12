import streamlit as st
from custom_css_file import get_custom_css_page

# Function to handle the create account page
def get_create_account_page():
    get_custom_css_page(alignment="left")

    st.title("Create Your Account")
    st.write("Enter your Bentley University email and password to sign up")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    
    # Variable to determine if user is admin or student
    is_admin = email == "admin@falcon.bentley.edu"
    
    # Add checkbox for agreeing to the Terms and Conditions only for students
    agree_terms = False
    if not is_admin:  # Show checkbox only for students
        agree_terms = st.checkbox("I agree to the Terms and Conditions")
    
    submit_clicked = st.button("Submit")
    
    if submit_clicked:
        # If the user is a student and hasn't agreed to the terms
        if not is_admin and not agree_terms:
            st.error("You must agree to the Terms and Conditions to continue.")
        # Check if the email ends with @falcon.bentley.edu 
        elif not email.endswith("@falcon.bentley.edu") or email.count('@') != 1:
            st.error("Please enter a valid Bentley University email address.")
        elif is_admin:  # If admin, navigate to admin landing page
            st.session_state.page = "admin_landing_page"
            st.success("Account created successfully!")
        else:  # If student, navigate to student landing page
            st.session_state.page = "student_landing_page"
            st.success("Account created successfully!")

