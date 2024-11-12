import streamlit as st
import random
from data.information import df  # Ensure this path is correct or adjust as needed

# Fake data for profiles
profiles = [
    {'name': 'Alice', 'age': 23, 'bio': 'Love to hike and travel!', 'image': 'https://randomuser.me/api/portraits/women/1.jpg'},
    {'name': 'Bob', 'age': 25, 'bio': 'Movie lover and pizza enthusiast.', 'image': 'https://randomuser.me/api/portraits/men/1.jpg'},
    {'name': 'Charlie', 'age': 28, 'bio': 'Tech geek and gamer.', 'image': 'https://randomuser.me/api/portraits/men/2.jpg'},
    {'name': 'Diana', 'age': 22, 'bio': 'Art lover and fashionista.', 'image': 'https://randomuser.me/api/portraits/women/2.jpg'},
    {'name': 'Eva', 'age': 27, 'bio': 'Foodie and fitness addict.', 'image': 'https://randomuser.me/api/portraits/women/3.jpg'},
    {'name': 'Frank', 'age': 30, 'bio': 'Traveler and photography enthusiast.', 'image': 'https://randomuser.me/api/portraits/men/3.jpg'},
]

# Function to display the profile
def display_profile(profile):
    st.image(profile['image'], width=200)
    st.write(f"**{profile['name']}, {profile['age']}**")
    st.write(profile['bio'])

# Set session state for keeping track of swipes
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0
if 'liked_profiles' not in st.session_state:
    st.session_state.liked_profiles = []
if 'disliked_profiles' not in st.session_state:
    st.session_state.disliked_profiles = []

# Check if there are profiles left to display
if st.session_state.current_index < len(profiles):
    current_profile = profiles[st.session_state.current_index]

    # Display the profile
    st.subheader("Swipe Right or Left")
    display_profile(current_profile)

    # Buttons for swipe actions
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button('❤️ Like'):
            st.session_state.liked_profiles.append(current_profile)
            # Move to next profile
            st.session_state.current_index += 1
        
    with col2:
        if st.button('❌ Dislike'):
            st.session_state.disliked_profiles.append(current_profile)
            # Move to next profile
            st.session_state.current_index += 1
else:
    st.write("No more profiles to show.")
    st.write("### Liked Profiles")
    for profile in st.session_state.liked_profiles:
        st.write(f"{profile['name']}, {profile['age']}")

    st.write("### Disliked Profiles")
    for profile in st.session_state.disliked_profiles:
        st.write(f"{profile['name']}, {profile['age']}")

