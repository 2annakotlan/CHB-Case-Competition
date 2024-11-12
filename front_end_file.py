# IMPORT PACKAGES AND OBJECTS 
from data_file import friend_swiping_df
from friend_swiping_file import get_friend_swiping_page
from login_signup_file import get_login_signup_page

import streamlit as st
import numpy as np
from PIL import Image
import requests
from io import BytesIO
import time

def load_image_from_url(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img

def blend_images(img1, img2, alpha):
    # Convert images to arrays and ensure they have the same size
    arr1 = np.array(img1)
    arr2 = np.array(img2)
    
    # Blend the images
    blended = (1 - alpha) * arr1 + alpha * arr2
    return blended.astype(np.uint8)

# Initialize session state
if 'alpha' not in st.session_state:
    st.session_state.alpha = 0.0
    st.session_state.direction = 1  # 1 for increasing, -1 for decreasing

# App title
st.title("Automatic Image Fade Effect")

# Load images
image_1 = load_image_from_url("https://github.com/2annakotlan/CHB-Case-Competition/raw/main/better_together_1.png")
image_2 = load_image_from_url("https://github.com/2annakotlan/CHB-Case-Competition/raw/main/better_together_2.png")

# Update alpha value
fade_speed = 0.02  # Adjust this value to control fade speed (smaller = slower)
st.session_state.alpha += fade_speed * st.session_state.direction

# Reverse direction if we reach the bounds
if st.session_state.alpha >= 1.0:
    st.session_state.alpha = 1.0
    st.session_state.direction = -1
elif st.session_state.alpha <= 0.0:
    st.session_state.alpha = 0.0
    st.session_state.direction = 1

# Blend the images based on current alpha
blended_image = blend_images(image_1, image_2, st.session_state.alpha)

# Display the blended image
st.image(blended_image, use_column_width=True)

# Add a small delay and rerun
time.sleep(0.1)  # Adjust this value to control animation smoothness
st.experimental_rerun()
