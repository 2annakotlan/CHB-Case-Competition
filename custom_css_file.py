import streamlit as st

# Function to apply custom CSS for background and styling
def get_custom_css_page():
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
            color: #4CAF50;
            font-family: 'Arial', sans-serif;
            font-weight: bold;
            margin-top: 20px;
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
            transition: background-color 0.3s ease;
        }
        
        .stButton button:hover {
            background-color: #45A049;
        }

        </style>
        """,
        unsafe_allow_html=True
    )
