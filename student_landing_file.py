import streamlit as st
from custom_css_file import get_custom_css_page

# Function to handle the student landing page view
def get_student_landing_page():
    get_custom_css_page(alignment="center", button_span="full")

    email_prefix = st.session_state.user_email.split('@')[0]
    formatted_prefix = f"{email_prefix[0].upper()}. {email_prefix[1:].capitalize()}"
    st.title(f"{formatted_prefix}'s Student Dashboard") 
    st.write(f"Welcome, {formatted_prefix}! This is your personal dashboard.")
    
    image_url_1 = "https://raw.githubusercontent.com/2annakotlan/CHB-Case-Competition/main/swipe.png"
    image_url_2 = "https://raw.githubusercontent.com/2annakotlan/CHB-Case-Competition/main/house.png"
    
    col1, col2 = st.columns(2)

    with col1:
        # Show image and use a button to set session_state.page on click
        if st.button("Friend Swiping", key="image1_button"):
            st.session_state.page = 'friend_swiping_page'
        st.image(image_url_1, width=300)

    with col2:
        # Show image and use a button to set session_state.page on click
        if st.button("Activities Recommender", key="image2_button"):
            st.session_state.page = 'friend_swiping_page'
        st.image(image_url_2, width=300)
    
    # Optionally, add a button to go back to the login/signup page
    if st.button('Log out'):
        st.session_state.page = "login_signup_page"

    if st.button('Edit Profile'):
        st.session_state.page = "profile_info_page"
