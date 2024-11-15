from custom_css_file import get_custom_css_page
from population_data_file import population_df
import streamlit as st

# Function to handle the sign-in page
def get_sign_in_page():
    get_custom_css_page(alignment="left", button_span="full")

    st.title("Admin Login")
    st.write("Enter admin email and password to sign in")
    
    email = st.text_input("Email", value="admin@falcon.bentley.edu", disabled=True)
    password = st.text_input("Password", type="password", value="123", disabled=True)
    
    # Defining Variables
    email_base = email.split('@')[0] 
    valid_existing_email = "admin@falcon.bentley.edu"  # Corrected to a string

    # Layout the buttons side by side using columns
    col1, col2 = st.columns([1, 1])
    
    with col1:
        back_clicked = st.button("Back")
    
    with col2:
        next_clicked = st.button("Next")
    
    if next_clicked:
        st.session_state.page = "admin_landing_page"

    if back_clicked:
        st.session_state.page = "login_signup_page"
