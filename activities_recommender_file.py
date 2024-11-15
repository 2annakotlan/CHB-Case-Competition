from custom_css_file import get_custom_css_page
import streamlit as st
from population_data_file import full_population_df
from activities_recommender_alg_file import get_activities
import pandas as pd

from custom_css_file import get_custom_css_page
import streamlit as st
from activities_recommender_alg_file import get_activities

def get_activities_recommender_page():
    get_custom_css_page(alignment="center", button_span="full")
    activities_df = get_activities(full_population_df, 'stest')
    
    # Filter and sort by 2nd-degree connections
    activities_df = activities_df[activities_df['count_degree_2'] > 0]
    activities_df = activities_df.sort_values(by='count_degree_2', ascending=False)
    
    # Display activities with the highest 2nd-degree connections first
    st.markdown("### 2nd Degree Connections")
    
    for _, row in activities_df.iterrows():
        count = row['count_degree_2']
        
        # Adjust for singular/plural usage
        people_word = "person" if count == 1 else "people"
        
        # Make activity name bold, pink, and larger font size
        activity_name = f"<span style='font-weight: bold; color: #FF1493; font-size: 22px;'>{row['activities']}</span>"
        
        # Construct the message
        message = f"Join {activity_name} to meet {count} new {people_word} that share a mutual friend."
        
        # Display the message with left-aligned text
        st.markdown(f"<div style='text-align: left;'>{message}</div>", unsafe_allow_html=True)
