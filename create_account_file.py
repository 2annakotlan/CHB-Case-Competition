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
    
    # Initialize checkbox for terms acceptance as None
    agree_terms = None

    # Add checkbox for agreeing to the Terms and Conditions only for students
    if not is_admin and email:  # Show checkbox only if the email is valid and not admin
        agree_terms = st.checkbox("I agree to the Terms and Conditions")

    submit_clicked = st.button("Submit")
    
    if submit_clicked:
        # 1. Validate the Bentley University email
        if not email.endswith("@falcon.bentley.edu") or email.count('@') != 1:
            st.error("Please enter a valid Bentley University email address.")
        
        # 2. If it’s a valid email and not an admin, check the Terms and Conditions
        elif not is_admin:
            if agree_terms is None:
                st.warning("Please confirm your acceptance of the Terms and Conditions.")  # Prompt to check terms if they haven't been shown yet
            elif not agree_terms:
                st.error("You must agree to the Terms and Conditions to continue.")
        
        # 3. Handle Admin or Student Role and Navigate
        elif is_admin:  # If admin, navigate to admin landing page
            st.session_state.page = "admin_landing_page"
            st.success("Account created successfully!")
        else:  # If student, navigate to student landing page
            st.session_state.page = "student_landing_page"
            st.success("Account created successfully!")
