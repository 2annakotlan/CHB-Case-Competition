import streamlit as st

def get_login_signup_page():
    # Title and Slogan
    st.markdown("<h1 style='text-align: center;'>Better Together</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>building an interconnected community</p>", unsafe_allow_html=True)

    # Center the buttons using HTML and CSS with rounded shapes and no borders
    st.markdown("""
        <style>
            .center-buttons {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
            }
            .stButton {
                margin: 15px;
                width: 200px;
                height: 50px;
                border-radius: 25px; /* Rounded corners */
                border: none;  /* No borders */
                background-color: #4CAF50; /* Green background */
                color: white;  /* White text */
                font-size: 16px;
                font-weight: bold;
                cursor: pointer;
                transition: background-color 0.3s ease;  /* Smooth background change on hover */
            }
            .stButton:hover {
                background-color: #45a049; /* Darker green on hover */
            }
        </style>
        <div class="center-buttons">
            <button class="stButton" id="create-account-button">Create Account</button>
            <button class="stButton" id="sign-in-button">Sign In</button>
        </div>
    """, unsafe_allow_html=True)

    # Display "Create Account" functionality
    if 'account_creation' not in st.session_state:
        st.session_state.account_creation = False

    # If Create Account button is clicked, show email input page
    if st.session_state.account_creation:
        st.markdown("<h2 style='text-align: center;'>Enter your Bentley University Email:</h2>", unsafe_allow_html=True)
        
        # Email input with autofill for "@falcon.bentley.edu"
        email_prefix = st.text_input("Your Bentley Email", value="", max_chars=50)
        
        # Append the domain automatically
        if email_prefix and not email_prefix.endswith("@falcon.bentley.edu"):
            email_prefix += "@falcon.bentley.edu"
        
        st.text_input("Full Email Address", value=email_prefix, disabled=True)

        # Next button
        if st.button("Next"):
            st.write(f"Email entered: {email_prefix}")
            # You can add further steps or logic here after the user clicks next.
            # For now, just display the email.

    # If Create Account button is clicked, set the account_creation state to True
    if st.button("Create Account"):
        st.session_state.account_creation = True

    # Sign In functionality can be added here if needed
    if st.button("Sign In"):
        st.write("Redirect to Sign In page...")
