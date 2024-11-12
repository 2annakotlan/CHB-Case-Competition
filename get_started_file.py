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
        if email == "admin@falcon.bentley.edu":  # Check if the email is admin
            st.session_state.page = "admin_landing_page"  # Go to admin landing page
        else:
            st.session_state.page = "student_landing_page"  # Go to student landing page
        st.success("Account created successfully!")

# Function to handle the sign-in page
def sign_in_page():
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

# Function to handle the admin landing page view
def admin_landing_page():
    st.title("Admin Dashboard")
    st.write("Welcome to the admin panel!")
    st.write("Here you can manage users, monitor activity, etc.")
    
    # Optionally, add a button to go back to the login/signup page
    if st.button('Log out'):
        st.session_state.page = "login_signup"

# Function to handle the student landing page view
def student_landing_page():
    st.title("Student Dashboard")
    st.write("Welcome, student! This is your personal dashboard.")
    st.write("Explore resources, courses, and more.")
    
    # Add buttons for "Friend Swiping" and "Activity Suggestions"
    if st.button("Friend Swiping"):
        st.session_state.page = "friend_swiping"  # Navigate to the friend-swiping page

    if st.button("Activity Suggestions"):
        st.session_state.page = "activity_suggestions"  # Navigate to the activity suggestions page
    
    # Optionally, add a button to go back to the login/signup page
    if st.button('Log out'):
        st.session_state.page = "login_signup"

# Function to control the flow of the app
def get_started_page():
    initialize_page_state()  # Initialize session state if necessary
    if st.session_state.page == 'login_signup':
        login_signup_page()  # Show the login/signup page
    elif st.session_state.page == 'create_account':
        create_account_page()  # Show the create account page
    elif st.session_state.page == 'sign_in':
        sign_in_page()  # Show the sign-in page
    elif st.session_state.page == 'admin_landing_page':
        admin_landing_page()  # Show the admin landing page
    elif st.session_state.page == 'student_landing_page':
        student_landing_page()  # Show the student landing page


