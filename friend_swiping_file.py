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

    # Store matches in the session state
    if "matched_people" not in st.session_state:
        st.session_state.matched_people = []

    # Get a random person from the population_df
    if len(population_df) > 0:
        person_index = random.choice(population_df.index)
        person = population_df.loc[person_index]
        
        # Person details
        name = person["0_degree"]
        interests = person["interests"]
        match_status = person["match"]

        # Random image for the person
        image_url = random.choice(random_images)

        # Display the profile info and image
        st.image(image_url, caption=f"{name}'s Profile", width=300)
        st.write(f"**Name:** {name}")
        st.write(f"**Interests:** {interests}")

        # Show match status (whether this person has matched with you)
        if match_status == 1:
            st.write(f"**Match Status:** This person has swiped right on you. It's a match!")
        else:
            st.write(f"**Match Status:** This person has not swiped right on you.")

        # Swipe buttons
        col1, col2 = st.columns(2)

        with col1:
            if st.button("Swipe Left", key=f"left_{person_index}"):
                st.write(f"You swiped left on {name}.")
        
        with col2:
            if st.button("Swipe Right", key=f"right_{person_index}"):
                # Update match status if you swipe right
                if match_status == 0:  # If they don’t already like you (match == 0)
                    population_df.at[person_index, "match"] = 1  # Update match status
                    st.session_state.matched_people.append(name)  # Add to matched list
                    st.write(f"You swiped right on {name}. It's a match!")

        # Display the matches below the current profile
        st.subheader("Your Matches:")
        if st.session_state.matched_people:
            for match in st.session_state.matched_people:
                st.write(match)
        else:
            st.write("No matches yet.")

    else:
        st.write("No profiles available to swipe.")

    # DONT REMOVE BELOW
    if st.button('Back to Dashboard'):
        st.session_state.page = "student_landing_page"

