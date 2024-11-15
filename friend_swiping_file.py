# PACKAGES
import streamlit as st
import pandas as pd
from custom_css_file import get_custom_css_page
from population_data_file import population_df

# GET TINDER-LIKE SWIPING VISUAL FUNCTION
def get_friend_swiping_page():
    # Apply custom CSS for styling
    get_custom_css_page()

    # Title of the page
    st.title("Tinder - Swipe Profiles")

    # Create a list of people you've matched with (will be shown on the sidebar)
    matched_people = []

    # Display the swipeable profiles
    for index, person in population_df.iterrows():
        name = person["0_degree"]
        interests = person["interests"]
        match_status = person["match"]

        # Display the profile info
        st.subheader(f"{name}'s Profile")
        st.write(f"Interests: {interests}")

        # Show the swipe options (buttons for right swipe and left swipe)
        swipe = st.radio(f"Do you like {name}?", ["Swipe Left", "Swipe Right"], key=name)

        # Handle swipe right (match)
        if swipe == "Swipe Right":
            if match_status == 0:  # if they don't already like you (match == 0)
                population_df.at[index, "match"] = 1  # Update the match status in the dataframe
                matched_people.append(name)  # Add the matched person to the list

        # Display matches in the sidebar
        st.sidebar.write("People You've Matched With:")
        st.sidebar.write(matched_people)

    # DONT REMOVE BELOW
    if st.button('Back to Dashboard'):
        st.session_state.page = "student_landing_page"


