import streamlit as st

st.markdown("<h1 style='font-size: 50px;'>BetterTogether</h1>", unsafe_allow_html=True)
if 'login' not in st.session_state:
    st.session_state.login = False

# Display login button
if not st.session_state.login:
    login_button = st.button("Login")

    if login_button:
        st.session_state.login = True

# If login button was pressed, show username and password inputs
if st.session_state.login:
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')

    if st.button("Submit"):
        # Handle authentication here (this is just a placeholder)
        if username == "admin" and password == "password":  # Example check
            st.success("Logged in successfully!")
        else:
            st.error("Invalid username or password.")
