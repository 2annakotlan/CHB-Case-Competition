# IMPORT PACKAGES AND OBJECTS 
from data_file import friend_swiping_df
from friend_swiping_file import get_friend_swiping_page
from get_started_file import get_started_page
import streamlit as st

get_started_page()

if st.session_state.page == 'friend_swiping':
    friend_swiping_page()
