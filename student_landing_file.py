import streamlit as st

# Function to handle the student landing page view
def get_student_landing_page():
    st.title("Student Dashboard")
    st.write("Welcome, student! This is your personal dashboard.")
    st.write("Explore resources, courses, and more.")
    
    # FontAwesome icons for Friend Swiping and Activity Suggestions
    col1, col2 = st.columns(2)
    
    with col1:
        if st.markdown('<i class="fa fa-users fa-5x"></i>', unsafe_allow_html=True):  # Example: friend swiping icon
            st.session_state.page = "friend_swiping_page"
    
    with col2:
        if st.markdown('<i class="fa fa-calendar-check fa-5x"></i>', unsafe_allow_html=True):  # Example: activity suggestions icon
            st.session_state.page = "activity_suggestions_page"
    
    # Optionally, add a button to go back to the login/signup page
    if st.button('Log out'):
        st.session_state.page = "login_signup_page"

    if st.button('Edit Profile'):
        st.session_state.page = "profile_info_page"
