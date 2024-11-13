import streamlit as st
from custom_css_file import get_custom_css_page
from population_data_file import population_df

# Function to handle the sign-in page
def get_sign_in_page():
    get_custom_css_page(alignment="left", button_span="full")

    st.title("Sign In")
    st.write("Enter your Bentley University email and password to sign in")
    
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    
    # Defining Variables
    valid_email = email.endswith("@falcon.bentley.edu") and email.count('@') == 1
    valid_student_email = valid_email and email != "admin@falcon.bentley.edu"
    valid_admin_email = email == "admin@falcon.bentley.edu"

    # Check if the email exists in the population data
    not_existing_email = email.split('@')[0] not in population_df['0_degree'].values

    # Initialize checkbox for terms acceptance
    agree_terms = st.checkbox("I agree to the terms and conditions.")
    
    enter_clicked = st.button("Enter")
    
    if enter_clicked:
        # 1. Validate the Bentley University email
        if not valid_email:
            st.error("Please enter a valid Bentley University email address.")
        
        # 2. Handle Admin Role Navigation
        elif valid_admin_email:  # If admin, navigate to admin landing page
            st.session_state.page = "admin_landing_page"

        # 3. Handle New Accounts
        elif not_existing_email:
            st.error("This account does not exist - create a new account.")

        # 4. Handle Student Role Navigation 
        elif valid_student_email:  # If student, navigate to student landing page
            st.session_state.user_email = email
            st.session_state.page = "student_landing_page"
        
        # 5. Check for terms acceptance
        if not agree_terms:
            st.error("You must agree to the terms and conditions.")
