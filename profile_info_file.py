import streamlit as st
import pandas as pd
from PIL import Image
from create_account_file import get_create_account_page
from custom_css_file import get_custom_css_page
from activities_interests_data_file import interests, activities
from population_data_file import population_df

def get_profile_info_page():
    # Apply custom CSS with specified alignment and button span
    get_custom_css_page(alignment="left", button_span="auto")
    
    # Format user's email prefix for the profile title
    email_prefix = st.session_state.user_email.split('@')[0]
    formatted_prefix = f"{email_prefix[0].upper()}. {email_prefix[1:].capitalize()}"
    st.title(f"{formatted_prefix}'s Profile") 
    
    # Collect user's 1st-degree connections
    selected_connections = st.text_input("Enter your friends (e.g., AKotlan, RMiller, SLogan, etc.)")
    
    # Predefined options for interests and activities from imported data files
    interest_options = interests
    activity_options = activities
    
    # Collect user's interests using a multi-select option without a default value
    selected_interests = st.multiselect("Select your interests", interest_options)
    
    # Collect user's activities using a multi-select option without a default value
    selected_activities = st.multiselect("Select your activities", activity_options)

    # Button to submit the profile information
    if st.button('Enter', use_container_width=False):
        formatted_connections = "{" + selected_connections.replace(" ", ";").replace(",", ";") + "}"
        formatted_activities = "{" + ";".join(selected_activities) + "}"
        formatted_interests = "{" + ";".join(selected_interests) + "}"
        
        # Check if the row with the email_prefix exists
        if email_prefix in population_df["0_degree"].values:
            population_df.loc[population_df["0_degree"] == email_prefix, ["1_degree", "activities", "interests"]] = [
                formatted_connections,
                formatted_activities,
                formatted_interests]
        else:
            new_row = {
                "0_degree": email_prefix,
                "1_degree": formatted_connections,
                "activities": formatted_activities,
                "interests": formatted_interests
            }
            population_df = population_df.append(new_row, ignore_index=True)
        
        # Set the session state to navigate to the student landing page
        st.session_state.page = "student_landing_page"
