import streamlit as st
from custom_css_file import get_custom_css_page

# Function to handle the create account page
def get_create_account_page():
    get_custom_css_page(alignment="left")

    st.title("Create Your Account")
    st.write("Enter your Bentley University email and password to sign up")

    # Email input with the @falcon.bentley.edu already filled and uneditable
    email_local = st.text_input("Email", value="", max_chars=50)

    # Construct the full email with the domain added
    email = email_local + "@falcon.bentley.edu"

    # Custom CSS to display the domain as grey text (non-editable)
    st.markdown(f"""
    <style>
        .stTextInput div[data-baseweb="input"] input {{
            padding-right: 200px; /* Adding space for the domain text */
        }}
        .stTextInput div[data-baseweb="input"]::after {{
            content: "@falcon.bentley.edu";
            color: grey;
            position: absolute;
            right: 0;
            top: 50%;
            transform: translateY(-50%);
            font-size: 14px;
        }}
    </style>
    """, unsafe_allow_html=True)

    # Password input
    password = st.text_input("Password", type="password")

    # Submit button action
    if st.button("Submit"):
        if email == "admin@falcon.bentley.edu":  # Check if the email is admin
            st.session_state.page = "admin_landing_page"  # Go to admin landing page
        else:
            st.session_state.page = "student_landing_page"  # Go to student landing page
        st.success("Account created successfully!")
