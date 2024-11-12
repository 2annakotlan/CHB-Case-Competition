# IMPORT PACKAGES AND OBJECTS 
from data_file import friend_swiping_df
from friend_swiping_file import get_friend_swiping_page
from login_signup_file import get_login_signup_page


import streamlit as st
import numpy as np
from PIL import Image
import requests
from io import BytesIO

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

# App title
st.title("Image Fade Effect")

# Load images
image_1 = load_image_from_url("https://github.com/2annakotlan/CHB-Case-Competition/raw/main/better_together_1.png")
image_2 = load_image_from_url("https://github.com/2annakotlan/CHB-Case-Competition/raw/main/better_together_2.png")

# Create a slider for controlling the fade effect
alpha = st.slider("Fade Control", 0.0, 1.0, 0.0, 0.01)

# Blend the images based on the slider value
blended_image = blend_images(image_1, image_2, alpha)

# Display the blended image
st.image(blended_image, use_column_width=True)
