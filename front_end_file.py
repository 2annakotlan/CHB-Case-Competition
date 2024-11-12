# IMPORT PACKAGES AND OBJECTS 
from data_file import friend_swiping_df
from friend_swiping_file import get_friend_swiping_page
import streamlit as st

# Function to initialize the page state if not already set
def get_initialize_page():
    if 'page' not in st.session_state:
        st.session_state.page = 'login_signup_page'  # Default starting page

# Function to handle the login/signup page view
def get_login_signup_page():
    st.title("Better Together")
    st.write("Building an interconnected community")

    # Buttons for navigating to the next pages
    if st.button('Create account'):
        st.session_state.page = "create_account_page"
    
    if st.button('Sign in'):
        st.session_state.page = "sign_in_page"

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

# Function to handle the admin landing page view
def get_admin_landing_page():
    st.title("Admin Dashboard")
    st.write("Welcome to the admin panel!")
    st.write("Here you can manage users, monitor activity, etc.")
    
    # Optionally, add a button to go back to the login/signup page
    if st.button('Log out'):
        st.session_state.page = "login_signup_page"

# Function to handle the student landing page view
def get_student_landing_page():
    st.title("Student Dashboard")
    st.write("Welcome, student! This is your personal dashboard.")
    st.write("Explore resources, courses, and more.")
    
    # Add buttons for "Friend Swiping" and "Activity Suggestions"
    if st.button("Friend Swiping"):
        st.session_state.page = "friend_swiping_page"  # Navigate to the friend-swiping page

    if st.button("Activity Suggestions"):
        st.session_state.page = "activity_suggestions_page"  # Navigate to the activity suggestions page
    
    # Optionally, add a button to go back to the login/signup page
    if st.button('Log out'):
        st.session_state.page = "login_signup_page"

get_initialize_page()  
if st.session_state.page == 'login_signup_page':
    get_login_signup_page()  
elif st.session_state.page == 'create_account_page':
    get_create_account_page()  
elif st.session_state.page == 'sign_in_page':
    get_sign_in_page()  
elif st.session_state.page == 'admin_landing_page':
    get_admin_landing_page()  
elif st.session_state.page == 'student_landing_page':
    get_student_landing_page()  
elif st.session_state.page == 'friend_swiping_page':  # Corrected to elif
    get_friend_swiping_page(friend_swiping_df)
