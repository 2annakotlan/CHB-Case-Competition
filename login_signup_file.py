import streamlit as st

def get_login_signup_page():
    # Center the title with a custom header style
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Better Together</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px; color: #6c757d;'>Building an interconnected community</p>", unsafe_allow_html=True)

    # Add some space before the buttons
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Center the buttons in a two-column layout
    col1, col2 = st.columns(2)

    with col1:
        if st.button('Create Account', use_container_width=True):
            st.session_state.page = "create_account_page"
    
    with col2:
        if st.button('Sign In', use_container_width=True):
            st.session_state.page = "sign_in_page"


