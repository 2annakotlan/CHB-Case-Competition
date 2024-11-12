import streamlit as st

def get_login_signup_page(image_url_1, image_url_2):
    # Define CSS for full-screen background with simultaneous fade transition
    st.markdown(
        f"""
        <style>
        /* Ensure the app container covers the entire screen */
        .stApp {{
            position: relative;
            width: 100%;
            height: 100%;
            overflow: hidden;
        }}
        
        /* Full-screen background image layers */
        .background {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-size: cover;
            background-position: center;
            transition: opacity 10s ease-in-out;
        }}

        /* Image 1 starts visible and fades out */
        .image1 {{
            background-image: url("{image_url_1}");
            opacity: 1;
            z-index: 1;
            animation: fadeOut 10s forwards;
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
        </style>

        <div class="stApp">
            <div class="background image1"></div>
            <div class="background image2"></div>
        </div>
        """,
        unsafe_allow_html=True
    )


