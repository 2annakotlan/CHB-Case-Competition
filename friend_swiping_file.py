# PACKAGES
import streamlit as st
import pandas as pd
from custom_css_file import get_custom_css_page
from population_data_file import population_df

# GET TINDER-LIKE SWIPING VISUAL FUNCTION
def get_tinder_swiping_page():
    # Apply custom CSS
    get_custom_css_page()

    # Title of the page
    st.title("Tinder - Swipe Profiles")

    # Initialize variables to keep track of the profile index and matches
    if 'profile_index' not in st.session_state:
        st.session_state.profile_index = 0
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
            # Just move to the next profile without changing the match list
            st.session_state.profile_index += 1
            if st.session_state.profile_index >= len(population_df):
                st.session_state.profile_index = 0  # Reset to the start if end of profiles
            st.experimental_rerun()

    with col2:
        if st.button('Swipe Right'):
            # Move to the next profile, and check for a match
            if profile['match'] == 1:  # They swiped right on me
                # If they swiped right on me too, it's a match
                matches.append(profile['0_degree'])  # Add their name to matches

            # Go to next profile after swiping right
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
