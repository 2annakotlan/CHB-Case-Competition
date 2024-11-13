# PACKAGES
import streamlit as st
import pandas as pd

# GET FRIEND SWIPING VISUAL FUNCTION
def get_friend_swiping_page(df):
   st.write("this is the friend swiping page!")

    # DONT REMOVE BELOW
    if st.button('Back to Dashboard'):
        st.session_state.page = "student_landing_page"
