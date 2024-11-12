# IMPORT PACKAGES AND OBJECTS 
from data_file import friend_swiping_df
from friend_swiping_file import get_friend_swiping_page
from login_signup_file import get_login_signup_page

import streamlit as st

# Set the page layout and title
st.set_page_config(page_title="Image Fade Transition Example")

# Example usage with two image URLs
image_1 = "https://github.com/2annakotlan/CHB-Case-Competition/raw/main/Better%20Together%201.png"
image_2 = "https://github.com/2annakotlan/CHB-Case-Competition/raw/main/Better%20Together%202.png"

# Inject custom CSS for the fade-in fade-out effect
st.markdown(
    f"""
    <style>
    /* Full page background setup */
    .stApp {{
        height: 100vh;
        overflow: hidden;
        position: relative;
    }}
    
    /* Image 1 (starting image) */
    .image1 {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: url("{image_1}");
        background-size: cover;
        background-position: center;
        opacity: 1;
        animation: fadeOut 5s forwards;
    }}
    
    /* Image 2 (new image) */
    .image2 {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: url("{image_2}");
        background-size: cover;
        background-position: center;
        opacity: 0;
        animation: fadeIn 5s forwards;
        animation-delay: 5s;  /* Delay to start after the first image fades */
    }}
    
    /* Fade-out animation */
    @keyframes fadeOut {{
        from {{
            opacity: 1;
        }}
        to {{
            opacity: 0;
        }}
    }}

    /* Fade-in animation */
    @keyframes fadeIn {{
        from {{
            opacity: 0;
        }}
        to {{
            opacity: 1;
        }}
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Add content to Streamlit
st.title("Image Fade Transition Example")
st.write("In this example, Image 1 fades out while Image 2 fades in.")
st.markdown("<div class='image1'></div>", unsafe_allow_html=True)
st.markdown("<div class='image2'></div>", unsafe_allow_html=True)
