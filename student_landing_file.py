import streamlit as st

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
