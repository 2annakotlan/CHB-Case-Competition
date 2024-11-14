import streamlit as st
from custom_css_file import get_custom_css_page
from population_data_file import population_df

def get_create_account_page():
    get_custom_css_page(alignment="left", button_span="auto")

    st.title("Create Your Account")
    st.write("Enter your Bentley University email and password to sign up")
    
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    
    # Defining Variables
    valid_email = email.endswith("@falcon.bentley.edu") 
    valid_admin_email = email == "admin@falcon.bentley.edu"
    email_base = email.split('@')[0]  # Get the username part of the email
    valid_existing_email = email_base in population_df['0_degree'].values
    valid_new_student_email = email != admin_email

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

        # 3. Handle pre-existing account
        elif pre_existing_email:
            st.error("This account already exists - go back and select sign in.")
        
        # 4. Handle student account creation and terms agreement
        elif valid_new_student_email: 
            if not agree_terms:
                st.error("You must agree to the Terms and Conditions to continue.")
            else:
                st.session_state.user_email = email
                st.session_state.page = "profile_info_page"
