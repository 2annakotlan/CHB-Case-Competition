# PACKAGES
import streamlit as st
import pandas as pd

# GET FRIEND SWIPING VISUAL FUNCTION
def get_friend_swiping_page(df):
    # Initialize session state variables
    if 'liked_profiles' not in st.session_state:
        st.session_state.liked_profiles = []
    if 'profile_index' not in st.session_state:
        st.session_state.profile_index = 0

    def show_profile(profile):
        st.image(profile['img'], width=300)
        st.write(f"**{profile['name']}, {profile['age']}**")
        st.write(f"_{profile['bio']}_")

    st.title("Friend Finder Swiping App")

    # Check if there are more profiles to show
    if st.session_state.profile_index < len(df):
        current_profile = df.iloc[st.session_state.profile_index]
        show_profile(current_profile)

        # Buttons for Like and Dislike
        col1, col2 = st.columns(2)
        with col1:
            if st.button("❤️ Like"):
                st.session_state.liked_profiles.append(current_profile)
                st.session_state.profile_index += 1
        with col2:
            if st.button("❌ Dislike"):
                st.session_state.profile_index += 1
    else:
        st.write("No more profiles to show!")

    # Show the list of liked profiles
    st.subheader("Liked Profiles")
    if st.session_state.liked_profiles:
        for _, liked in enumerate(st.session_state.liked_profiles):
            st.write(f"{liked['name']}, {liked['age']} - {liked['bio']}")
    else:
        st.write("You haven't liked anyone yet!")
