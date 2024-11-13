import streamlit as st
from PIL import Image
from create_account_file import get_create_account_page

def get_profile_info_page():
    # Title for the profile page
    st.title(f"{st.session_state.user_email}'s Profile")  # Fixed string formatting

    # Ask for the profile picture
    profile_picture = st.file_uploader("Upload your profile picture", type=["jpg", "png", "jpeg"])

    # If a profile picture is uploaded, display it
    if profile_picture is not None:
        img = Image.open(profile_picture)
        st.image(img, width=200)

    # Collect the user's name
    name = st.text_input("What's your name?", "John Doe")

    # Collect the user's age
    age = st.number_input("How old are you?", 18, 100, 25)

    # Collect the user's bio
    bio = st.text_area("Tell us a little about yourself:", "I love to code and build cool projects!")

    # Collect user's interests
    interests = st.text_input("What are your interests?", "Coding, Music, Hiking")

    # Option for a short tagline or quote
    tagline = st.text_input("Your personal tagline or quote:", "Dream big, work hard!")

    # Show the collected information
    st.subheader("Profile Information")

    # Display email from session state
    st.write(f"**Email:** {st.session_state.user_email}")  # Corrected the email display
    st.write(f"**Name:** {name}")
    st.write(f"**Age:** {age}")
    st.write(f"**Bio:** {bio}")
    st.write(f"**Interests:** {interests}")
    st.write(f"**Tagline:** {tagline}")

    # Add a button to submit and view the profile
    if st.button('Submit'):
        st.success("Profile Updated Successfully!")
