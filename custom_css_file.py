import streamlit as st

# In custom_css_file.py, rename the function to get_custom_css_page
def get_custom_css_page(alignment="center"):
    """
    Applies custom CSS to style the Streamlit page.

    Parameters:
    - alignment (str): Align both text and buttons to "center" or "left".
    """
    # Define alignment for both text and buttons
    align = "center" if alignment == "center" else "left"

    # Add custom CSS for background and other styles
    st.markdown(
        f"""
        <style>
        /* Background with gradient */
        .stApp {{
            background: linear-gradient(135deg, #E0F7FA, #FFEBEE);
            background-size: cover;
        }}
        
        /* Text alignment */
        h1, p {{
            text-align: {align};
        }}
        
        /* Title style */
        h1 {{
            color: #4CAF50;
            font-family: 'Arial', sans-serif;
            font-weight: bold;
            margin-top: 20px;
        }}
        
        p {{
            font-size: 18px;
            color: #6c757d;
            margin-bottom: 30px;
        }}
        
        /* Button style */
        .stButton button {{
            width: 100%;
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            padding: 10px 20px;
            border-radius: 10px;
            border: none;
            transition: background-color 0.3s ease;
        }}
        
        .stButton button:hover {{
            background-color: #45A049;
        }}
        
        /* Align buttons (left or center) */
        .stButton {{
            display: flex;
            justify-content: {align};
        }}

        </style>
        """,
        unsafe_allow_html=True
    )
