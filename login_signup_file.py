import streamlit as st

def get_login_signup_page(image_url_1, image_url_2):
    # Define CSS for full-screen background with simultaneous fade transition
    st.markdown(
        f"""
        <style>
        /* Ensure the app container is full-screen */
        .stApp {{
            position: relative;
            width: 100vw;
            height: 100vh;
            overflow: hidden;
            margin: 0; /* No margin */
            padding: 0; /* No padding */
        }}
        
        /* Full-screen background image layers */
        .background {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-size: 100% 100%; /* Stretch images to fill the entire viewport */
            background-position: center;
            transition: opacity 2s ease-in-out;
        }}

        /* Image 1 starts visible and fades out */
        .image1 {{
            background-image: url("{image_url_1}");
            opacity: 1;
            z-index: 1;
            animation: fadeOut 10s forwards; /* Fade out image 1 over time */
        }}

        /* Image 2 starts invisible and fades in */
        .image2 {{
            background-image: url("{image_url_2}");
            opacity: 0;
            z-index: 2;
            animation: fadeIn 10s forwards;
            animation-delay: 0s; /* Image 2 fades in immediately */
        }}

        /* Keyframes for fading out image 1 */
        @keyframes fadeOut {{
            0%   {{ opacity: 1; }}
            100% {{ opacity: 0; }}
        }}

        /* Keyframes for fading in image 2 */
        @keyframes fadeIn {{
            0%   {{ opacity: 0; }}
            100% {{ opacity: 1; }}
        }}

        /* Centered button container */
        .button-container {{
            position: relative;
            z-index: 3;
            display: flex;
            justify-content: center;
            gap: 20px;
            top: 45%;
        }}

        /* Styling for login and sign-up buttons */
        .button {{
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            border: none;
            border-radius: 5px;
            background-color: #ffffff;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
        }}
        </style>

        <!-- HTML structure for background images and buttons -->
        <div class="stApp">
            <div class="background image1"></div>
            <div class="background image2"></div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Streamlit buttons for Login and Sign Up
    col1, col2 = st.columns(2)
    with col1:
        if st.button('Login'):
            st.write('Login clicked')
    with col2:
        if st.button('Sign Up'):
            st.write('Sign Up clicked')
