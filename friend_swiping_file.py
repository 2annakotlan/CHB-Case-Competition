# PACKAGES
import streamlit as st
import pandas as pd
from custom_css_file import get_custom_css_page

# GET FRIEND SWIPING VISUAL FUNCTION
def get_friend_swiping_page():
   get_custom_css_page()
   st.title("Friend Swiping")
   

    # DONT REMOVE BELOW
   if st.button('Back to Dashboard'):
      st.session_state.page = "student_landing_page"
