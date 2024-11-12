# IMPORT PACKAGES AND OBJECTS 
from data_file import friend_swiping_df
from friend_swiping_file import get_friend_swiping_page
from login_file import get_login_signup_page, get_create_account_page, get_sign_in_page
from landing_file import get_admin_landing_page, get_student_landing_page
import streamlit as st

initialize_page_state()  
if st.session_state.page == 'login_signup':
    get_login_signup_page()  
elif st.session_state.page == 'create_account':
    get_create_account_page()  
elif st.session_state.page == 'sign_in':
    get_sign_in_page()  
elif st.session_state.page == 'admin_landing_page':
    get_admin_landing_page()  
elif st.session_state.page == 'student_landing_page':
    get_student_landing_page()  
if st.session_state.page == 'friend_swiping':
    get_friend_swiping_page(friend_swiping_df)


