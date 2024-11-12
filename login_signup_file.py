import streamlit as st

def get_login_signup_page():
    # Adding custom CSS to set the background color and center buttons
    st.markdown(
        """
        <style>
        .main {
            background-color: #1E3A8A;  /* Dark blue color */
            height: 100vh; /* Full viewport height */
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }

        .stButton button {
            background-color: #4CAF50; /* Green background */
            color: white; /* White text */
            padding: 12px 24px;
            font-size: 16px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: background-color 0.3s ease;
            width: 200px; /* Fixed width for consistent centering */
            margin-top: 10px; /* Space between buttons */
        }

        .stButton button:hover {
            background-color: #45a049; /* Darker green on hover */
        }

        /* Center the title and description text */
        .centered-content {
            text-align: center;
            margin-bottom: 20px;
        }
        </style>
        """, unsafe_allow_html=True)

    # Centered title and description at the top of the page
    st.markdown('<div class="centered-content">', unsafe_allow_html=True)
    st.title("Better Together")
    st.write("Building an interconnected community")
    st.markdown('</div>', unsafe_allow_html=True)

    # Buttons for navigating to the next pages
    if st.button('Create account'):
        st.session_state.page = "create_account_page"

    if st.button('Sign in'):
        st.session_state.page = "sign_in_page"
