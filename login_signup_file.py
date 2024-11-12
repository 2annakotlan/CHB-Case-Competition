import streamlit as st

def get_login_signup_page(image_url_1, image_url_2):
    # Define CSS for full-screen background and animation
    st.markdown(
        f"""
        <style>
        .stApp {{
            height: 100vh;
            overflow: hidden;
            position: relative;
        }}
        .background {{
            position: absolute;
            width: 100%;
            height: 100%;
            background-size: cover;
            background-position: center;
            animation: fadeAnimation 10s infinite alternate;
        }}
        .image1 {{
            background-image: url("{image_url_1}");
            opacity: 0; /* Start as invisible */
            animation-delay: 0s;
        }}
        .image2 {{
            background-image: url("{image_url_2}");
            opacity: 1; /* Start as visible */
            animation-delay: 5s;
        }}
        
        @keyframes fadeAnimation {{
            0% {{ opacity: 1; }}
            50% {{ opacity: 0; }}
            100% {{ opacity: 1; }}
        }}

        .button-container {{
            position: relative;
            z-index: 2;
            display: flex;
            justify-content: center;
            gap: 20px;
            top: 45%;
        }}

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
        <div class="stApp">
            <div class="background image1"></div>
            <div class="background image2"></div>
            <div class="button-container">
                <button class="button" onclick="alert('Login clicked')">Login</button>
                <button class="button" onclick="alert('Sign Up clicked')">Sign Up</button>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


