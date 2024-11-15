from custom_css_file import get_custom_css_page
import streamlit as st
from activities_recommender_alg_file import get_activities

def get_activities_recommender_page():
    get_custom_css_page(alignment="center", button_span="full")
    activities_df = get_activities(full_population_df, 'stest')
    
    # Filter and sort by 2nd-degree connections
    activities_df['total_people'] = activities_df['count_degree_2']
    activities_df = activities_df[activities_df['total_people'] > 0]
    activities_df = activities_df.sort_values(by='count_degree_2', ascending=False)
    
    # Display activities with the highest 2nd-degree connections first
    st.markdown("### 2nd Degree Connections")
    
    for _, row in activities_df.iterrows():
        total_people = row['total_people']
        message = f"Join **{row['activities']}** to meet {total_people} new people that share a mutual friend."
        st.markdown(f"<div style='text-align: left;'>{message}</div>", unsafe_allow_html=True)
