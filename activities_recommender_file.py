from custom_css_file import get_custom_css_page
import streamlit as st
from population_data_file import full_population_df
from activities_recommender_alg_file import get_activities
import pandas as pd

def get_activities_recommender_page():
    get_custom_css_page(alignment="center", button_span="full")
    activities_df = get_activities(full_population_df, 'stest')
    
    # Big title with custom style
    st.markdown("<h1 style='text-align: center; font-size: 36px; color: #FF1493;'>Activities Recommendation</h1>", unsafe_allow_html=True)
    
    # Subheading with nice text
    st.markdown("<h3 style='text-align: center;'>Activities to Meet Mutual Friends</h3>", unsafe_allow_html=True)

    # Add some space between the list and the DataFrame
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <style>
        .streamlit-table {
            background-color: #f9f9f9;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }
        .streamlit-table th {
            background-color: #FF1493;
            color: white;
            font-weight: bold;
        }
        .streamlit-table td {
            padding: 10px;
            text-align: left;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Filter and sort by 2nd-degree connections
    activities_df = activities_df[activities_df['count_degree_2'] > 0]
    activities_df = activities_df.sort_values(by='count_degree_2', ascending=False)
    
    # Display activities with the highest 2nd-degree connections first
    for _, row in activities_df.iterrows():
        count = row['count_degree_2']
        
        # Adjust for singular/plural usage
        people_word = "person" if count == 1 else "people"
        share_word = "shares" if count == 1 else "share"
        
        # Make activity name bold, pink, and larger font size
        activity_name = f"<span style='font-weight: bold; color: #FF1493; font-size: 22px;'>{row['activities']}</span>"
        
        # Construct the message
        message = f"Join {activity_name} to meet {count} new {people_word} that {share_word} a mutual friend."
        
        # Display the message with left-aligned text
        st.markdown(f"<div style='text-align: left;'>{message}</div>", unsafe_allow_html=True)

    # Add some space before the DataFrame
    st.markdown("<br>", unsafe_allow_html=True)

    # Display DataFrame with styling
    st.dataframe(activities_df.style.set_table_attributes('class="streamlit-table"'))
