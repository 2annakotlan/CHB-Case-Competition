import streamlit as st

def get_login_signup_page():
    # Title centered using HTML and CSS
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
            }
        </style>
        <div class="centered">
            <div class="title">Better Together</div>
            <div class="subtitle">Building an interconnected community</div>
            <div class="button-container">
                <button onclick="window.location.href='/button1'">Button 1</button>
                <button onclick="window.location.href='/button2'">Button 2</button>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Action when buttons are clicked
    if st.button('Button 1'):
        st.write('You clicked Button 1!')
    
    if st.button('Button 2'):
        st.write('You clicked Button 2!')
