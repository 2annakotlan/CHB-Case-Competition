import streamlit as st

def get_login_signup_page(image_url_2):
    # Define custom CSS to set the background image
    page_bg_img = f"""
    <style>
    .stApp {{
        background-image: url("{image_url_2}");
        background-size: cover;
        background-position: center;
        height: 100vh;
    }}
    </style>
    """
    # Inject the CSS into the Streamlit app
    st.markdown(page_bg_img, unsafe_allow_html=True)

    # Create a simple layout with just the login and signup buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Login"):
            # Code for login functionality here
            pass
    with col2:
        if st.button("Signup"):
            # Code for signup functionality here
            pass
