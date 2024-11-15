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
    
    # Sort by degree of connection first (1-degree, 2-degree, etc.), then by total_people within each degree group
    degree_columns = [col for col in activities_df.columns if col.startswith('count_degree')]
    degree_columns_sorted = sorted(degree_columns, key=lambda x: int(x.split('_')[-1]))  # Sorting by degree number
    
    # Create a column to sort by degree first, then total_people
    activities_df['degree_priority'] = activities_df.apply(
        lambda row: [row[col] for col in degree_columns_sorted], axis=1
    )
    
    activities_df = activities_df.sort_values(by=['degree_priority', 'total_people'], ascending=[True, False])

    st.dataframe(activities_df)
    generate_activities_messages(activities_df)

    for _, row in activities_df.iterrows():
        total_people = row['total_people']

        # Determine the message based on the number of people
        if total_people == 1:
            message = f"Join <span style='font-size: 18px; font-weight: bold; color: #ff5733;'>{row['activities']}</span> to meet 1 new person that shares a mutual friend."
        else:
            message = f"Join <span style='font-size: 18px; font-weight: bold; color: #ff5733;'>{row['activities']}</span> to meet {total_people} new people that share a mutual friend."

        # Use Markdown with HTML for better styling
        st.markdown(f"<div style='text-align: left;'>{message}</div>", unsafe_allow_html=True)
