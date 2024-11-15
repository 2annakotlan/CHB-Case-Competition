from custom_css_file import get_custom_css_page
import streamlit as st
from population_data_file import full_population_df
from activities_recommender_alg_file import get_activities
import pandas as pd

def get_activities_recommender_page():
    get_custom_css_page(alignment="center", button_span="full")
    activities_df = get_activities(full_population_df, 'stest')
    
    # Exclude '1_degree' columns from total_people calculation
    activities_df['total_people'] = activities_df.apply(
        lambda row: sum(row[col] for col in row.index if col.startswith('count_degree') and col != 'count_degree_1'), axis=1
    )
    
    # Sort activities by total_people in descending order
    activities_df = activities_df.sort_values(by='total_people', ascending=False)
    
    st.dataframe(activities_df)

    for _, row in activities_df.iterrows():
        total_people = row['total_people']

        # Determine the message based on the number of people
        if total_people == 1:
            message = f"Join {row['activities']} to meet 1 person in your social network."
        else:
            message = f"Join {row['activities']} to meet {total_people} people in your social network."

        # Use Markdown to center the message
        st.markdown(f"<div style='text-align: center;'>{message}</div>", unsafe_allow_html=True)
