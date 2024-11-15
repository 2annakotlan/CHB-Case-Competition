# PACKAGES
import streamlit as st
import pandas as pd
import random
from custom_css_file import get_custom_css_page
from population_data_file import population_df

# Sample list of random images (replace with your own image URLs or file paths)
random_images = [
    "https://randomuser.me/api/portraits/men/1.jpg",
    "https://randomuser.me/api/portraits/women/1.jpg",
    "https://randomuser.me/api/portraits/men/2.jpg",
    "https://randomuser.me/api/portraits/women/2.jpg",
    "https://randomuser.me/api/portraits/men/3.jpg",
    "https://randomuser.me/api/portraits/women/3.jpg"
]

# GET TINDER-LIKE SWIPING VISUAL FUNCTION
def get_friend_swiping_page():
    # Apply custom CSS for styling
    get_custom_css_page()

    # Title of the page
    st.title("Tinder - Swipe Profiles")

    # Store the list of names you've swiped right on in the session state
    if "swiped_right" not in st.session_state:
        st.session_state.swiped_right = []

    # Get a random person from the population_df
    if len(population_df) > 0:
        person_index = random.choice(population_df.index)
        person = population_df.loc[person_index]
        
        # Person details
        name = person["0_degree"]
        interests = person["interests"]

        # Random image for the person
        image_url = random.choice(random_images)

        # If the person is swiped right, show the match message first
        if name in st.session_state.swiped_right:
            st.write(f"**You swiped right on {name}. It's a match!**")

        # Format interests nicely as a comma-separated list
        formatted_interests = ", ".join(sorted(interests))  # Sort for better readability

        # Add CSS for centering the image
        st.markdown("""
            <style>
                .profile-image {
                    display: block;
                    margin-left: auto;
                    margin-right: auto;
                    width: 300px;
                }
            </style>
        """, unsafe_allow_html=True)

        # Display the profile info and image (using the CSS class to center the image)
        st.image(image_url, caption=f"{name}'s Profile", use_column_width=False, class_="profile-image")

        st.write(f"**Interests:** {formatted_interests}")

        # Swipe buttons
        col1, col2 = st.columns(2)

        with col1:
            if st.button("Swipe Left", key=f"left_{person_index}"):
                st.write(f"You swiped left on {name}.")
        
        with col2:
            if st.button("Swipe Right", key=f"right_{person_index}"):
                # Add to the list of people you swiped right on
                if name not in st.session_state.swiped_right:
                    st.session_state.swiped_right.append(name)  # Add to list of people you've swiped right on
                    st.write(f"**You swiped right on {name}. It's a match!**")

        # Display the list of people you've swiped right on as bullet points
        st.subheader("Your Matches:")
        if st.session_state.swiped_right:
            for match in st.session_state.swiped_right:
                st.markdown(f"- {match}")
        else:
            st.write("No matches yet.")

    else:
        st.write("No profiles available to swipe.")

    # DONT REMOVE BELOW
    if st.button('Back to Dashboard'):
        st.session_state.page = "student_landing_page"


