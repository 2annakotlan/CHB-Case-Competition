# PACKAGES
import streamlit as st
import pandas as pd
#from custom_css_file import get_custom_css_page
#from population_data_file import population_df

# Use the provided image URL for every profile
#image_url = "https://github.com/2annakotlan/CHB-Case-Competition/blob/main/phone-book.png?raw=true"  # The "?raw=true" is required for GitHub image links

# GET TINDER-LIKE SWIPING VISUAL FUNCTION
def get_friend_swiping_page():
    # Apply custom CSS for styling
    #get_custom_css_page()

    # Title of the page
    st.title("Friend Swiping")
    
    # Back to dashboard button
    if st.button('Back to Dashboard'):
        st.session_state.page = "student_landing_page"
