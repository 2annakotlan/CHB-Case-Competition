# IMPORT PACKAGES AND OBJECTS 
from data_file import friend_swiping_df
from friend_swiping_file import get_friend_swiping_page
from login_file import get_initialize_page, get_login_signup_page, get_create_account_page, get_signin_page
from landing_file import get_admin_landing_page, get_student_landing_page
import streamlit as st

get_initialize_page()  
if st.session_state.page == 'login_signup_page':
    get_login_signup_page()  
elif st.session_state.page == 'create_account_page':
    get_create_account_page()  
elif st.session_state.page == 'sign_in_page':
    get_sign_in_page()  
elif st.session_state.page == 'admin_landing_page':
    get_admin_landing_page()  
elif st.session_state.page == 'student_landing_page':
    get_student_landing_page()  
elif st.session_state.page == 'friend_swiping_page':  # Corrected to elif
    get_friend_swiping_page(friend_swiping_df)
