# IMPORT PACKAGES AND OBJECTS 
from data_file import friend_swiping_df
from friend_swiping_file import get_friend_swiping_page
from login_signup_file import get_login_signup_page


# Example usage with two image URLs
image_url_1 = "https://github.com/2annakotlan/CHB-Case-Competition/raw/main/Better Together 1.png"
image_url_2 = "https://github.com/2annakotlan/CHB-Case-Competition/raw/main/Better Together 2.png"
get_login_signup_page(image_url_2)

#get_friend_swiping_page(friend_swiping_df)

import streamlit as st
import json

# Custom JavaScript to fetch the screen size
js_code = """
    <script>
        const screenDimensions = {
            width: window.innerWidth,
            height: window.innerHeight
        };
        const dimensions = JSON.stringify(screenDimensions);
        const data = new CustomEvent('screenDimensions', { detail: dimensions });
        window.dispatchEvent(data);
    </script>
"""

# HTML to display the image and dimensions
html_code = """
    <div>
        <h3>Screen Proportions</h3>
        <p>Width: {0}</p>
        <p>Height: {1}</p>
        <p>Aspect Ratio (Width/Height): {2}</p>
    </div>
"""

# Function to fetch and display screen size
def get_screen_size():
    st.markdown(js_code, unsafe_allow_html=True)
    # Wait for JavaScript to update screen size
    st.session_state.screen_size = None

    def handle_screen_dimensions(event):
        data = json.loads(event["detail"])
        st.session_state.screen_size = data

    # Listen for the custom event
    st.components.v1.html(f"""
        <script>
            window.addEventListener("screenDimensions", function(event) {{
                const data = JSON.parse(event.detail);
                const width = data.width;
                const height = data.height;
                const aspect_ratio = (width / height).toFixed(2);
                document.getElementById("screen-dimensions").innerHTML = `
                    Width: ${width}px<br>
                    Height: ${height}px<br>
                    Aspect Ratio: ${aspect_ratio}
                `;
            }});
        </script>
    """, height=0)
    
    if st.session_state.screen_size:
        width = st.session_state.screen_size["width"]
        height = st.session_state.screen_size["height"]
        aspect_ratio = width / height
        st.markdown(html_code.format(width, height, round(aspect_ratio, 2)))
        
# Show the screen proportions
get_screen_size()
