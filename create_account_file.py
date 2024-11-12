import streamlit as st
from custom_css_file import get_custom_css_page

# Function to handle the create account page
def get_create_account_page():
    #get_custom_css_page(alignment="left")

    st.title("Create Your Account")
    st.write("Enter your Bentley University email and password to sign up")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    
    # Add checkbox for agreeing to the Terms and Conditions
    agree_terms = st.checkbox("I agree to the Terms and Conditions")

    if st.button("Submit"):
        # Check if the email ends with @falcon.bentley.edu 
        if not email.endswith("@falcon.bentley.edu") or email.count('@') != 1:
            st.error("Please enter a valid Bentley University email address")
        elif email == "admin@falcon.bentley.edu":  # Check if the email is admin
            st.session_state.page = "admin_landing_page"  # Go to admin landing page
            st.success("Account created successfully!")
        else:
            st.session_state.page = "student_landing_page"  # Go to student landing page
            st.success("Account created successfully!")
        
    # Display checkbox status (this part is just for visual feedback)
    if agree_terms:
        st.write("You have agreed to the Terms and Conditions.")
    else:
        st.write("Please agree to the Terms and Conditions to continue.")
