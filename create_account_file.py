import streamlit as st
from custom_css_file import get_custom_css_page
from population_data_file import population_df

def get_create_account_page():
    get_custom_css_page(alignment="left", button_span="full")

    st.title("Create Your Account")
    st.write("Enter your Bentley University email and password to sign up")
    
    email = st.text_input("Email", value="stest@falcon.bentley.edu", disabled=True)
    password = st.text_input("Password", type="password", value="123", disabled=True)
    
    # Defining Variables
    valid_email = email.endswith("@falcon.bentley.edu")
    admin_email = email == "admin@falcon.bentley.edu"
    email_base = email.split('@')[0]  
    valid_existing_email = email_base in population_df['0_degree'].values and email.endswith("@falcon.bentley.edu") and not admin_email
    valid_not_existing_email = email_base not in population_df['0_degree'].values and email.endswith("@falcon.bentley.edu") and not admin_email

    # Initialize checkbox for terms acceptance only for new students
    agree_terms = st.checkbox("I agree to the Terms and Conditions") if valid_not_existing_email else None

    # Layout the buttons side by side using columns
    col1, col2 = st.columns([1, 1])
    
    with col1:
        back_clicked = st.button("Back")
    
    with col2:
        next_clicked = st.button("Next")
    
    if next_clicked:
        # 1. Validate Bentley University email
        if not valid_email:
            st.error("Please enter a valid Bentley University email address.")
        
        # 2. Handle admin account navigation
        elif admin_email: 
            st.session_state.page = "admin_landing_page"

        # 3. Handle pre-existing student account
        elif valid_existing_email:
            st.error("This account already exists - go back and select sign in.")
        
        # 4. Handle new student account creation and terms agreement
        elif valid_not_existing_email:
            if not agree_terms:
                st.error("You must agree to the Terms and Conditions to continue.")
            else:
                st.session_state.user_email = email
                st.session_state.page = "profile_info_page"

    if back_clicked:
        st.session_state.page = "login_signup_page"  
