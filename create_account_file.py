import streamlit as st
from custom_css_file import get_custom_css_page

def get_create_account_page():
    get_custom_css_page(alignment="left", button_span="full")

    st.title("Create Your Account")
    st.write("Enter your Bentley University email and password to sign up")
    
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    
    # Defining Variables
    valid_email = email.endswith("@falcon.bentley.edu") and email.count('@') == 1
    valid_student_email = valid_email and email != "admin@falcon.bentley.edu"
    valid_admin_email = email == "admin@falcon.bentley.edu"

    # Initialize checkbox only for students with valid email
    agree_terms = st.checkbox("I agree to the Terms and Conditions") if valid_student_email else None
    
    submit_clicked = st.button("Submit")
    
    if submit_clicked:
        # 1. Validate Bentley University email
        if not valid_email:
            st.error("Please enter a valid Bentley University email address.")
        
        # 2. Handle admin account creation
        elif valid_admin_email: 
            st.session_state.page = "admin_landing_page"
        
        # 3. Handle student account creation and terms agreement
        elif valid_student_email: 
            if not agree_terms:
                st.error("You must agree to the Terms and Conditions to continue.")
            else:
                st.session_state.user_email = email
                st.session_state.page = "profile_info_page"
