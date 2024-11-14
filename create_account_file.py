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
    email_base = email.split('@')[0] 
    valid_not_existing_email = stest@falcon.bentley.edu

    # Initialize checkbox for terms acceptance only for new students
    agree_terms = st.checkbox("I agree to the Terms and Conditions") if valid_not_existing_email else None

    # Layout the buttons side by side using columns
    col1, col2 = st.columns([1, 1])
    
    with col1:
        back_clicked = st.button("Back")
    
    with col2:
        next_clicked = st.button("Next")
    
    if next_clicked:
        if valid_not_existing_email:
            if not agree_terms:
                st.error("You must agree to the Terms and Conditions to continue.")
            else:
                st.session_state.user_email = email
                st.session_state.page = "profile_info_page"

    if back_clicked:
        st.session_state.page = "login_signup_page"  
