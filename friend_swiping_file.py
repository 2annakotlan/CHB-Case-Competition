# PACKAGES
import streamlit as st
import pandas as pd
import random
from custom_css_file import get_custom_css_page
from population_data_file import population_df

# Use the provided image URL for every profile
image_url = "https://github.com/2annakotlan/CHB-Case-Competition/blob/main/phone-book.png?raw=true"  # The "?raw=true" is required for GitHub image links

# GET TINDER-LIKE SWIPING VISUAL FUNCTION
def get_friend_swiping_page():
    # Apply custom CSS for styling
    get_custom_css_page()

    # Title of the page
    st.title("Friend Swiping")

    # Initialize session states for swipes if not already done
    if "swiped_right" not in st.session_state:
        st.session_state.swiped_right = []
    if "shown_people" not in st.session_state:
        st.session_state.shown_people = []
    if "liked_you" not in st.session_state:
        st.session_state.liked_you = []

    # Filter out the row where 0_degree is "Liam" and already shown people
    filtered_population_df = population_df[population_df["0_degree"] != "Liam"]
    remaining_population_df = filtered_population_df[~filtered_population_df.index.isin(st.session_state.shown_people)]

    # Ensure there are people left to swipe
    if len(remaining_population_df) > 0:
        # Select a random person from the remaining profiles
        person_index = random.choice(remaining_population_df.index)
        person = remaining_population_df.loc[person_index]
        
        # Extract person details
        name = person["0_degree"]
        interests = person["interests"]

        # Display match message if the person has been swiped right
        if name in st.session_state.swiped_right:
            st.write(f"**You swiped right on {name}. It's a match!**")
        
        # Format interests as a comma-separated list and sort for readability
        formatted_interests = ", ".join(sorted(interests))

        # Add custom CSS for centering profile elements
        st.markdown("""
            <style>
                .profile-image {
                    display: block;
                    margin-left: auto;
                    margin-right: auto;
                    width: 300px;
                }
                .profile-name {
                    display: block;
                    text-align: center;
                    font-size: 24px;
                    font-weight: bold;
                    margin-top: 10px;
                }
            </style>
        """, unsafe_allow_html=True)

        # Display the profile image and name centered
        st.markdown(f'<img src="{image_url}" class="profile-image">', unsafe_allow_html=True)
        st.markdown(f'<div class="profile-name">{name}\'s Profile</div>', unsafe_allow_html=True)

        # Display the person's interests
        st.write(f"**Interests:** {formatted_interests}")

        # Create swipe buttons
        col1, col2 = st.columns(2)

        with col1:
            if st.button("Swipe Left", key=f"left_{person_index}"):
                st.write(f"You swiped left on {name}.")
                st.session_state.shown_people.append(person_index)  # Mark as shown
        
        with col2:
            if st.button("Swipe Right", key=f"right_{person_index}"):
                if name not in st.session_state.swiped_right:
                    st.session_state.swiped_right.append(name)
                    st.write(f"**You swiped right on {name}. It's a match!**")
                
                # Simulate that some people might "like" you back by randomly adding to liked_you
                if random.random() < 0.5:  # 50% chance they "like" you
                    st.session_state.liked_you.append(name)
                
                st.session_state.shown_people.append(person_index)  # Mark as shown

        # Display the list of matches (with email suffix)
        st.subheader("Your Matches:")
        if st.session_state.swiped_right:
            for match in st.session_state.swiped_right:
                email_match = f"{match}@falcon.bentley.edu"
                liked_status = " (Liked you!)" if match in st.session_state.liked_you else ""
                st.markdown(f"- {email_match}{liked_status}")
        else:
            st.write("No matches yet.")

    else:
        st.write("No profiles available to swipe.")

    # Return to the dashboard when the button is clicked
    if st.button('Back to Dashboard'):
        st.session_state.page = "student_landing_page"
