import streamlit as st
import random

# Sample data for profiles (in a real app, this would be fetched from a database)
profiles = [
    {"name": "Alex", "age": 25, "bio": "Loves hiking and the outdoors.", "img": "https://randomuser.me/api/portraits/men/10.jpg"},
    {"name": "Taylor", "age": 22, "bio": "Avid reader and aspiring writer.", "img": "https://randomuser.me/api/portraits/women/21.jpg"},
    {"name": "Jordan", "age": 28, "bio": "Tech enthusiast and gamer.", "img": "https://randomuser.me/api/portraits/men/33.jpg"},
    {"name": "Morgan", "age": 24, "bio": "Foodie and world traveler.", "img": "https://randomuser.me/api/portraits/women/45.jpg"},
    {"name": "Chris", "age": 30, "bio": "Music producer and DJ.", "img": "https://randomuser.me/api/portraits/men/67.jpg"}
]

# Initialize session state to keep track of likes and current profile index
if 'liked_profiles' not in st.session_state:
    st.session_state.liked_profiles = []
if 'profile_index' not in st.session_state:
    st.session_state.profile_index = 0

def show_profile(profile):
    """Display the current profile."""
    st.image(profile["img"], width=300)
    st.write(f"**{profile['name']}, {profile['age']}**")
    st.write(f"_{profile['bio']}_")

# Main app interface
st.title("Tinder-Like App in Streamlit")

# Check if there are more profiles to show
if st.session_state.profile_index < len(profiles):
    current_profile = profiles[st.session_state.profile_index]
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
    for liked in st.session_state.liked_profiles:
        st.write(f"{liked['name']}, {liked['age']} - {liked['bio']}")
else:
    st.write("You haven't liked anyone yet!")
