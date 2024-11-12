import streamlit as st

def get_login_signup_page():
    # Add custom CSS for centering
    st.markdown("""
        <style>
            .centered {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
            }
            .title {
                font-size: 32px;
                font-weight: bold;
            }
            .subtitle {
                font-size: 18px;
                margin-bottom: 30px;
            }
            .button-container {
                display: flex;
                gap: 20px;
                justify-content: center;
            }
        </style>
    """, unsafe_allow_html=True)

    # Title and subtitle
    st.markdown('<div class="centered">', unsafe_allow_html=True)
    st.markdown('<div class="title">Better Together</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Building an interconnected community</div>', unsafe_allow_html=True)

    # Create two buttons, and place them in the center
    button1_clicked = st.button('Button 1')
    button2_clicked = st.button('Button 2')

    # Display corresponding message when buttons are clicked
    if button1_clicked:
        st.write('You clicked Button 1!')
    
    if button2_clicked:
        st.write('You clicked Button 2!')

    st.markdown('</div>', unsafe_allow_html=True)

