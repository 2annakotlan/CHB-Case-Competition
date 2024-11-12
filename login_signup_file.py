import streamlit as st

def get_login_signup_page():
    st.title("Better Together")
    st.write("Building an interconnected community")

    # Buttons for navigating to the next pages
    if st.button('Create account'):
        st.session_state.page = "create_account_page"

    if st.button('Sign in'):
        st.session_state.page = "sign_in_page"

