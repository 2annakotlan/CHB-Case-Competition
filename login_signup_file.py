import streamlit as st

def get_login_signup_page(image_url_1, image_url_2):
    # Add a slider to control the transition between images
    blend_factor = st.slider("Transition Factor", 0.0, 1.0, 0.5, label_visibility="hidden")
    
    # CSS for the background images with adjustable opacity
    st.markdown(
        f"""
        <style>
        .stApp {{
            position: relative;
            height: 100vh;
            overflow: hidden;
        }}
        .background {{
            position: absolute;
            width: 100%;
            height: 100%;
            background-size: cover;
            background-position: center;
        }}
        .image1 {{
            background-image: url("{image_url_1}");
            opacity: {1 - blend_factor};
            z-index: 1;
        }}
        .image2 {{
            background-image: url("{image_url_2}");
            opacity: {blend_factor};
            z-index: 2;
        }}
        .button-container {{
            position: relative;
            z-index: 3;
            text-align: center;
            top: 40%;
        }}
        </style>
        <div class="stApp">
            <div class="background image1"></div>
            <div class="background image2"></div>
            <div class="button-container">
                <div style="display: inline-block; margin: 10px;">
                    <button onclick="alert('Login clicked')" style="padding: 10px 20px; font-size: 16px;">Login</button>
                </div>
                <div style="display: inline-block; margin: 10px;">
                    <button onclick="alert('Sign Up clicked')" style="padding: 10px 20px; font-size: 16px;">Sign Up</button>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

