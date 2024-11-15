import streamlit as st

# In custom_css_file.py, rename the function to get_custom_css_page
def get_custom_css_page(alignment="center", button_span="full"):
    # Define alignment for both text and buttons
    align = "center" if alignment == "center" else "left"
    
    # Define button span style based on the 'button_span' parameter
    if button_span == "full":
        button_width = "100%"
    else:
        button_width = "auto"  # Default button width, not full span

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
            color: #4A90E2;
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
            width: {button_width};
            background-color: #4A90E2;
            color: white;
            font-size: 16px;
            padding: 10px 20px;
            border-radius: 10px;
            border: none;
            transition: background-color 0.3s ease;
        }}
        
        .stButton button:hover {{
            background-color: #4A90E2;
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
