import streamlit as st

def get_login_signup_page():
    # Add custom CSS for background styling with an overlay pattern
    st.markdown(
        """
        <style>
        /* Background with gradient and shape overlay */
        .stApp {
            background: linear-gradient(135deg, #E0F7FA, #FFEBEE);
            background-size: cover;
            position: relative;
            overflow: hidden;
        }

        /* Adding translucent circles as overlay */
        .stApp::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: radial-gradient(circle at 10% 20%, rgba(255, 182, 193, 0.2), transparent),
                        radial-gradient(circle at 80% 80%, rgba(144, 224, 239, 0.2), transparent),
                        radial-gradient(circle at 50% 50%, rgba(255, 234, 167, 0.15), transparent);
            z-index: -1; /* Places overlay behind all content */
        }

        /* Center and style title with shadow */
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
            text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.1);
        }

        /* Customize button appearance with shadow and hover effect */
        .stButton button {
            width: 100%;
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            padding: 10px 20px;
            border-radius: 10px;
            border: none;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            transition: background-color 0.3s ease, box-shadow 0.3s ease;
        }
        
        .stButton button:hover {
            background-color: #45A049;
            box-shadow: 0px 6px 8px rgba(0, 0, 0, 0.15);
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


