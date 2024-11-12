import streamlit as st

def get_login_signup_page():
    # Title and Slogan
    st.markdown("<h1 style='text-align: center;'>Better Together</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>building an interconnected community</p>", unsafe_allow_html=True)

    # Centered Button Layout
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
    """, unsafe_allow_html=True)

    # Check if account_creation flag exists, if not, set it to False
    if 'account_creation' not in st.session_state:
        st.session_state.account_creation = False

    # Show the main page with buttons for Create Account or Sign In
    if not st.session_state.account_creation:
        # Center buttons
        st.markdown('<div class="center-buttons">', unsafe_allow_html=True)

        # "Create Account" Button
        if st.button('Create Account'):
            st.session_state.account_creation = True
        
        # "Sign In" Button
        if st.button('Sign In'):
            st.write("Redirect to Sign In page...")
        
        st.markdown('</div>', unsafe_allow_html=True)

    # If Create Account is clicked, show the email input page
    if st.session_state.account_creation:
        st.markdown("<h2 style='text-align: center;'>Enter your Bentley University Email:</h2>", unsafe_allow_html=True)

        # Email input field (user only types the part before @falcon.bentley.edu)
        email_prefix = st.text_input("Your Bentley Email", value="", max_chars=50)

        # Append the domain automatically if it's not already present
        if email_prefix and not email_prefix.endswith("@falcon.bentley.edu"):
            email_prefix += "@falcon.bentley.edu"
        
        # Display the full email (disabled to prevent editing)
        st.text_input("Full Email Address", value=email_prefix, disabled=True)

        # Next button
        if st.button("Next"):
            st.write(f"Email entered: {email_prefix}")
            # Additional logic for next steps can be added here
