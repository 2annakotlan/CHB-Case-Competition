import streamlit as st
from custom_css_file import get_custom_css_page

# Function to handle the create account page
def get_create_account_page():
    get_custom_css_page(alignment="left")

    st.title("Create Your Account")
    st.write("Enter your Bentley University email and password to sign up")
    
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    
    # Defining Variables
    valid_email = email.endswith("@falcon.bentley.edu") and email.count('@') == 1
    valid_student_email = valid_email and email != "admin@falcon.bentley.edu"
    valid_admin_email = email == "admin@falcon.bentley.edu"

    # Initialize checkbox for terms acceptance as None
    agree_terms = None
    
    # Add checkbox for agreeing to the Terms and Conditions only for students
    if valid_student_email:  # Show checkbox only if the email is valid and not admin
        tooltip = """
        <span class="tooltip">
            I agree to the Terms and Conditions
            <span class="tooltiptext">By agreeing, you accept the terms that govern your use of our platform, including our privacy policy and data usage rules.</span>
        </span>
        """
        # Render the checkbox with a tooltip
        agree_terms = st.checkbox(tooltip, unsafe_allow_html=True)
    
    submit_clicked = st.button("Submit")
    
    if submit_clicked:
        # 1. Validate the Bentley University email
        if not valid_email:
            st.error("Please enter a valid Bentley University email address.")
        
        # 2. If it’s a valid student email, check the Terms and Conditions
        elif valid_student_email:
            if not agree_terms:
                st.error("You must agree to the Terms and Conditions to continue.")
        
        # 3. Handle Admin Role Navigation
        elif valid_admin_email:  # If admin, navigate to admin landing page
            st.session_state.page = "admin_landing_page"
            st.success("Account created successfully!")

        # 4. Handle Student Role Navigation (this part was modified)
        elif valid_student_email:  # If student, navigate to student landing page
            st.session_state.page = "student_landing_page"
            st.success("Account created successfully!")
