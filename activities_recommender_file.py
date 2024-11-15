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
    
    # Filter for only 2nd-degree connections (count_degree_2)
    degree_activities = activities_df[activities_df['count_degree_2'] > 0]

    # Initialize an empty set to keep track of already printed activities
    printed_activities = set()

    # If there are no activities with 2nd-degree connections, skip
    if degree_activities.empty:
        st.markdown("No activities found with 2nd-degree connections.")
        return

    # Print the header for 2nd-degree connections
    st.markdown("### 2nd Degree Connections")

    for _, row in degree_activities.iterrows():
        # Skip activities that have already been printed
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
