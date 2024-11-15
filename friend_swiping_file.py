# PACKAGES
import streamlit as st
import pandas as pd
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

    # Initialize a list to hold your matches
    matches = []

    # Create a session state variable to track the current index of profiles
    if "current_profile" not in st.session_state:
        st.session_state.current_profile = 0

    # Get the current profile
    person = population_df.iloc[st.session_state.current_profile]

    # Extract person details
    name = person["0_degree"]
    interests = person["interests"]
    liked_you = person["match"] == 1  # Check if they liked you (match == 1)

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

    # Show whether they liked you or not
    if liked_you:
        st.write(f"**{name} liked you!**")
    else:
        st.write(f"**{name} has not liked you yet.**")

    # Create swipe buttons
    col1, col2 = st.columns(2)

    with col1:
        if st.button(f"Swipe Left on {name}", key=f"left_{st.session_state.current_profile}"):
            st.write(f"You swiped left on {name}.")
            # Move to the next profile
            st.session_state.current_profile += 1
        
    with col2:
        if st.button(f"Swipe Right on {name}", key=f"right_{st.session_state.current_profile}"):
            # Register the right swipe and check if it's a match
            if liked_you:
                matches.append(name)
                st.write(f"**You swiped right on {name}. It's a match!**")
            else:
                st.write(f"You swiped right on {name}. Waiting for them to like you back.")
            # Move to the next profile
            st.session_state.current_profile += 1

    # Display the list of matches (with email suffix)
    st.subheader("Your Matches:")
    if matches:
        for match in matches:
            email_match = f"{match}@falcon.bentley.edu"
            st.markdown(f"- {email_match}")
    else:
        st.write("No matches yet.")

    # Return to the dashboard when the button is clicked
    if st.button('Back to Dashboard'):
        st.session_state.page = "student_landing_page"
