from custom_css_file import get_custom_css_page
import streamlit as st
from population_data_file import full_population_df
from activities_recommender_alg_file import get_activities
import pandas as pd

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
        message = f"Join **{row['activities']}** to meet {count} new people that share a mutual friend."
        st.markdown(f"<div style='text-align: left;'>{message}</div>", unsafe_allow_html=True)
