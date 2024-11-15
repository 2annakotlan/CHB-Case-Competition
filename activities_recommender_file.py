from custom_css_file import get_custom_css_page
import streamlit as st
from population_data_file import full_population_df
from activities_recommender_alg_file import get_activities
import pandas as pd

def get_activities_recommender_page():
    get_custom_css_page(alignment="center", button_span="full")
    activities_df = get_activities(full_population_df, 'stest')
    st.dataframe(activities_df)

    for _, row in activities_df.iterrows():
        degree_columns = [col for col in row.index if col.startswith('count_degree')]
        total_people = row[degree_columns].sum()
        message = f"Meet {total_people} people in your social circle by joining {row['activities']}: "
        degree_message_parts = []
        
        for degree_col in degree_columns:
            count = row[degree_col]
            degree = degree_col.split('_')[-1]  # Extract the degree number
            
            if count > 0:
                if count == 1:
                    degree_message_parts.append(f"one person {degree} degree away")
                else:
                    degree_message_parts.append(f"{count} people {degree} degrees away")
        
        if len(degree_message_parts) > 1:
            message += ', '.join(degree_message_parts[:-1]) + ', and ' + degree_message_parts[-1]
        else:
            message += degree_message_parts[0]  # If only one part, just add it
        
        st.write(message)  # Display the message in Streamlit
