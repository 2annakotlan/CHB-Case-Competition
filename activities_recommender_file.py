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
    
    # Filter out activities with 0 total people
    activities_df = activities_df[activities_df['total_people'] > 0]
    
    # Initialize an empty set to keep track of already printed activities
    printed_activities = set()

    # Degree levels to filter and sort by (2-degree, 3-degree, etc.)
    degree_levels = ['count_degree_2', 'count_degree_3', 'count_degree_4', 'count_degree_5']

    for degree in degree_levels:
        # Filter activities that have non-zero people in the current degree
        degree_activities = activities_df[activities_df[degree] > 0]
        
        # Skip if no activities for this degree level
        if degree_activities.empty:
            continue

        # Print the header for the current degree level
        st.markdown(f"### {degree.replace('count_degree_', '').replace('_', ' ').title()} Connections")

        for _, row in degree_activities.iterrows():
            # Check if the activity was already printed in a previous degree section
            if row['activities'] in printed_activities:
                continue

            total_people = row['total_people']

            # Determine the message based on the number of people
            if total_people == 1:
                message = f"Join <span style='font-size: 18px; font-weight: bold; color: #ff5733;'>{row['activities']}</span> to meet 1 new person that shares a mutual friend."
            else:
                message = f"Join <span style='font-size: 18px; font-weight: bold; color: #ff5733;'>{row['activities']}</span> to meet {total_people} new people that share a mutual friend."

            # Use Markdown with HTML for better styling
            st.markdown(f"<div style='text-align: left;'>{message}</div>", unsafe_allow_html=True)

            # Mark this activity as printed
            printed_activities.add(row['activities'])

