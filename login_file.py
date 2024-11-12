import streamlit as st

# Function to initialize the page state if not already set
def get_initialize_page():
    if 'page' not in st.session_state:
        st.session_state.page = 'login_signup_page'  # Default starting page

# Function to handle the login/signup page view
def get_login_signup_page():
    st.title("Better Together")
    st.write("Building an interconnected community")

    # Custom CSS for styled, centered buttons in a vertical layout
    st.markdown(
        """
        <style>
        .button-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-top: 20px;
        }

        .stButton button {
            background-color: #4CAF50; /* Green background */
            color: white; /* White text */
            padding: 12px 24px;
            font-size: 16px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: background-color 0.3s ease;
            width: 200px; /* Fixed width to center the buttons */
            margin-top: 10px; /* Space between buttons */
        }

        .stButton button:hover {
            background-color: #45a049; /* Darker green on hover */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Centered, stacked buttons
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    
    if st.button('Create account'):
        st.session_state.page = "create_account_page"
    
    if st.button('Sign in'):
        st.session_state.page = "sign_in_page"

    st.markdown('</div>', unsafe_allow_html=True)


# Function to handle the create account page
def get_create_account_page():
    st.title("Create Your Account")
    st.write("Enter your school email and password to sign up")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Submit"):
        if email == "admin@falcon.bentley.edu":  # Check if the email is admin
            st.session_state.page = "admin_landing_page"  # Go to admin landing page
        else:
            st.session_state.page = "student_landing_page"  # Go to student landing page
        st.success("Account created successfully!")

# Function to handle the sign-in page
def get_sign_in_page():
    st.title("Sign In")
    st.write("Enter your email and password to sign in")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Sign In"):
        if email == "admin@falcon.bentley.edu":  # Check if the email is admin
            st.session_state.page = "admin_landing_page"  # Go to admin landing page
        else:
            st.session_state.page = "student_landing_page"  # Go to student landing page
        st.success("You are signed in successfully!")
