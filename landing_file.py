# Function to handle the admin landing page view
def get_admin_landing_page():
    st.title("Admin Dashboard")
    st.write("Welcome to the admin panel!")
    st.write("Here you can manage users, monitor activity, etc.")
    
    # Optionally, add a button to go back to the login/signup page
    if st.button('Log out'):
        st.session_state.page = "login_signup"

# Function to handle the student landing page view
def get_student_landing_page():
    st.title("Student Dashboard")
    st.write("Welcome, student! This is your personal dashboard.")
    st.write("Explore resources, courses, and more.")
    
    # Optionally, add a button to go back to the login/signup page
    if st.button('Log out'):
        st.session_state.page = "login_signup"

