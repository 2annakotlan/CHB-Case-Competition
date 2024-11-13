import streamlit as st
from PIL import Image
from create_account_file import get_create_account_page

def get_profile_info_page():
    # Ensure user_email exists in session state before using it
    if 'user_email' not in st.session_state:
        st.error("User is not logged in. Please create an account first.")
        return

    email_prefix = st.session_state.user_email.split('@')[0]
    st.title(f"{email_prefix}'s Profile") 

    # Ask for the profile picture
    profile_picture = st.file_uploader("Upload your profile picture", type=["jpg", "png", "jpeg"])

    # If a profile picture is uploaded, display it
    if profile_picture is not None:
        img = Image.open(profile_picture)
        st.image(img, width=200)

    # Collect user's 1st-degree connections
    one_degree_connections = st.text_input("What are your 1st-degree connections?", "John, Sarah, Mike")

    # Collect user's interests
    interests = st.text_input("What are your interests?", "Coding, Music, Hiking")

    # Collect user's activities
    activities = st.text_input("What are your activities?", "Coding, Music, Hiking")

    # Collect user's name, age, bio, and tagline
    name = st.text_input("What is your name?")
    age = st.number_input("What is your age?", min_value=0, max_value=120, value=25)
    bio = st.text_area("Write a short bio about yourself")
    tagline = st.text_input("What is your tagline?")

    # Show the collected information
    st.subheader("Profile Information")

    # Display email from session state
    st.write(f"**Email:** {st.session_state.user_email}")  # Corrected the email display
    st.write(f"**Name:** {name}")
    st.write(f"**Age:** {age}")
    st.write(f"**Bio:** {bio}")
    st.write(f"**Interests:** {interests}")
    st.write(f"**Tagline:** {tagline}")
    st.write(f"**1st-degree connections:** {one_degree_connections}")

    # Add a button to submit and view the profile
    if st.button('Submit'):
        st.success("Profile Updated Successfully!")
