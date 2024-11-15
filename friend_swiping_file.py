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

    # List to track the people swiped right
    swiped_right = []

    # Filter out the row where 0_degree is "Liam"
    filtered_population_df = population_df[population_df["0_degree"] != "Liam"]

    # Iterate over the rows in population_df
    for index, person in filtered_population_df.iterrows():
        name = person["0_degree"]
        interests = person["interests"]

        # Display the profile image and name centered
        st.markdown(f'<img src="{image_url}" class="profile-image">', unsafe_allow_html=True)
        st.markdown(f'<div class="profile-name">{name}\'s Profile</div>', unsafe_allow_html=True)

        # Format and display the person's interests
        formatted_interests = ", ".join(sorted(interests))
        st.write(f"**Interests:** {formatted_interests}")

        # Create swipe buttons
        col1, col2 = st.columns(2)

        with col1:
            if st.button("Swipe Left", key=f"left_{index}"):
                st.write(f"You swiped left on {name}.")
        
        with col2:
            if st.button("Swipe Right", key=f"right_{index}"):
                if name not in swiped_right:
                    swiped_right.append(name)  # Add to the swiped_right list
                    st.write(f"**You swiped right on {name}. It's a match!**")

        # After one swipe interaction, break out to let the user decide when to move to the next person
        break

    # Check if there are no profiles left
    if len(filtered_population_df) == 0:
        st.write("Done! You've swiped on all available profiles.")

    # Display the list of matches (with email suffix)
    st.subheader("Your Matches:")
    if swiped_right:
        for match in swiped_right:
            email_match = f"{match}@falcon.bentley.edu"
            st.markdown(f"- {email_match}")
    else:
        st.write("No matches yet.")

    # Return to the dashboard when the button is clicked
    if st.button('Back to Dashboard'):
        st.session_state.page = "student_landing_page"
