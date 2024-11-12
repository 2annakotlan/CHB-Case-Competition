import streamlit as st

def get_login_signup_page():
    # Add custom CSS for background styling
    st.markdown(
        """
        <style>
        /* Animated background with gradient */
        @keyframes gradientAnimation {
            0% {background-position: 0% 50%;}
            50% {background-position: 100% 50%;}
            100% {background-position: 0% 50%;}
        }
        
        .stApp {
            background: linear-gradient(135deg, #E0F7FA, #FFEBEE, #FFCDD2, #E1F5FE);
            background-size: 200% 200%;
            animation: gradientAnimation 10s ease infinite;
        }

        /* Optional overlay pattern for subtle texture */
        .stApp::before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-image: url('https://www.transparenttextures.com/patterns/cubes.png');
            opacity: 0.1;
            z-index: -1;
        }

        /* Center and style title and subtitle */
        h1 {
            text-align: center;
            color: #4CAF50;
            font-family: 'Arial', sans-serif;
            font-weight: bold;
            margin-top: 20px;
            text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
        }
        
        p {
            text-align: center;
            font-size: 18px;
            color: #6c757d;
            margin-bottom: 30px;
        }

        /* Customize button appearance */
        .stButton button {
            width: 100%;
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            padding: 10px 20px;
            border-radius: 10px;
            border: none;
            transition: background-color 0.3s ease, transform 0.2s ease;
        }
        
        .stButton button:hover {
            background-color: #45A049;
            transform: scale(1.05);
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    # Center the title and subtitle
    st.markdown("<h1>Better Together</h1>", unsafe_allow_html=True)
    st.markdown("<p>Building an interconnected community</p>", unsafe_allow_html=True)

    # Add spacing and create two-column layout for buttons
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button('Create Account', use_container_width=True):
            st.session_state.page = "create_account_page"
    
    with col2:
        if st.button('Sign In', use_container_width=True):
            st.session_state.page = "sign_in_page"


