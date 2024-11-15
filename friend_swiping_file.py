# PACKAGES
import streamlit as st
import pandas as pd
from custom_css_file import get_custom_css_page
from population_data_file import population_df

# GET TINDER-LIKE SWIPING VISUAL FUNCTION
def get_friend_swiping_page():
    # Apply custom CSS
    get_custom_css_page()

    # Title of the page
    st.title("Tinder - Swipe Profiles")

    # Initialize a local variable for profile index (starting from 0)
    if 'profile_index' not in st.session_state:
        st.session_state.profile_index = 0

    # Initialize matches list (to keep track of matches)
    matches = []

    # Load the profile data (assuming 'population_df' contains the profiles)
    profile = population_df.iloc[st.session_state.profile_index]

    # Display profile information
    st.write(f"Name: {profile['0_degree']}")
    st.write(f"Interests: {profile['interests']}")
    
    # Check if there is a match (this is based on their 'match' status)
    match_status = "Yes" if profile['match'] == 1 else "No"
    st.write(f"Matched: {match_status}")

    # Buttons for swiping left or right
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button('Swipe Left'):
            # Move to the next profile without changing the match list
            st.session_state.profile_index += 1
            if st.session_state.profile_index >= len(population_df):
                st.session_state.profile_index = 0  # Reset to the start if end of profiles
            st.experimental_rerun()

    with col2:
        if st.button('Swipe Right'):
            # Check for a match after swiping right
            if profile['match'] == 1:  # If the person swiped right on you
                # If both swiped right on each other, it's a match
                matches.append(profile['0_degree'])  # Add their name to matches

            # Move to the next profile after swiping right
            st.session_state.profile_index += 1
            if st.session_state.profile_index >= len(population_df):
                st.session_state.profile_index = 0  # Reset to the start if end of profiles
            st.experimental_rerun()

    # Display the list of matches
    if matches:
        st.subheader("Your Matches:")
        for match in matches:
            st.write(match)

    # DONT REMOVE BELOW
    if st.button('Back to Dashboard'):
        st.session_state.page = "student_landing_page"
