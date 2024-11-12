# IMPORT PACKAGES AND OBJECTS 
from data_file import friend_swiping_df
from friend_swiping_file import get_friend_swiping_page
from login_signup_file import get_login_signup_page


# Example usage with two image URLs
image_path = "https://github.com/2annakotlan/CHB-Case-Competition/raw/main/Better Together 1.png"
image_url_2 = "https://github.com/2annakotlan/CHB-Case-Competition/raw/main/Better Together 2.png"

#get_friend_swiping_page(friend_swiping_df)

import streamlit as st

# Set the page layout and title
st.set_page_config(page_title="Background Image Example")

# Define the path to your image file or URL
#image_path = "path_to_your_image.jpg"  # Replace with your image file or URL

# Inject custom CSS to set the background image
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{image_path}");
        background-size: cover;
        background-position: center;
        height: 100vh;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Add some content
st.title("Streamlit Background Image Example")
st.write("This is an example of setting an image as the background in Streamlit.")


