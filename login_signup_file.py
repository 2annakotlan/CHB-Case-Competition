import streamlit as st

def get_login_signup_page():
    st.title("Better Together")
    st.write("building an interconnected commuity")

    # Create two buttons with different labels
    if st.button('Button 1'):
        st.write('You clicked Button 1!')
    
    if st.button('Button 2'):
        st.write('You clicked Button 2!')

