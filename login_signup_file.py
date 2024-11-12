import streamlit as st

def get_login_signup_page():
    # Add custom CSS for background and text styling
    st.markdown(
        """
        <style>
        /* Background with gradient */
        .stApp {
            background: linear-gradient(135deg, #E0F7FA, #FFEBEE);
            background-size: cover;
        }
        
        /* Center and style title and subtitle */
        h1 {
            text-align: center;
            color: #1E88E5;  /* Blue color for the title */
            font-family: 'Arial', sans-serif;
            font-weight: bold;
            margin-top: 20px;
        }
        
        p {
            text-align: center;
            font-size: 18px;
            color: white;  /* White subtitle text */
            margin-bottom: 30px;
        }

        /* Customize button appearance */
        .stButton button {
            width: 100%;
            background-color: #1E88E5;  /* Blue button color */
            color: white;  /* White button text */
            font-size: 16px;
            padding: 10px 20px;
            border-radius: 10px;
            border: none;
            transition: background-color 0.3s ease;
        }
        
        .stButton button:hover {
            background-color: #1565C0;  /* Darker blue on hover */
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    # Center the title and subtitle with updated colors
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

