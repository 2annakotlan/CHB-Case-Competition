import streamlit as st

# Function to initialize the page state if not already set
def initialize_page_state():
    if 'page' not in st.session_state:
        st.session_state.page = 'login_signup'  # Default starting page

# Function to handle the login/signup page view
def login_signup_page():
    st.title("Better Together")
    st.write("Building an interconnected community")

    # Buttons for navigating to the next pages
    if st.button('Create account'):
        st.session_state.page = "create_account"
    
    if st.button('Sign in'):
        st.session_state.page = "sign_in"

# Function to handle the create account page
def create_account_page():
    st.title("Create Your Account")
    st.write("Enter your school email and password to sign up")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Submit"):
        st.session_state.page = "landing_page"  # Go to landing page after account creation
        st.success("Account created successfully!")

# Function to handle the sign-in page
def sign_in_page():
    st.title("Sign In")
    st.write("Enter your email and password to sign in")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Sign In"):
        st.session_state.page = "landing_page"  # Go to landing page after sign-in
        st.success("You are signed in successfully!")

# Function to handle the landing page view
def landing_page():
    st.title("Welcome to the Landing Page!")
    st.write("You have successfully signed in or created your account.")
    st.write("Explore our community and get started with your journey.")
    
    # Optionally, add a button to go back to the login/signup page
    if st.button('Log out'):
        st.session_state.page = "login_signup"

# Function to control the flow of the app
def get_started_page():
    # Initialize session state if necessary
    initialize_page_state()

    if st.session_state.page == 'login_signup':
        login_signup_page()  # Show the login/signup page
    elif st.session_state.page == 'create_account':
        create_account_page()  # Show the create account page
    elif st.session_state.page == 'sign_in':
        sign_in_page()  # Show the sign-in page
    elif st.session_state.page == 'landing_page':
        landing_page()  # Show the landing page after successful login/signup


