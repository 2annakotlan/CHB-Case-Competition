from custom_css_file import get_custom_css_page
import streamlit as st
from population_data_file import full_population_df
from algorithm import get_activities
import pandas as pd

def get_activities_recommender_page():
    get_custom_css_page(alignment="center", button_span="full")
    
    # Get the activities DataFrame from the algorithm
    activities_df = get_activities(full_population_df, 'stest')

    # Debug: Check columns in the activities DataFrame
    st.write(activities_df.columns)  # This will print the column names in the activities_df DataFrame
    
    # Check if 'count_degree_2' column exists
    if 'count_degree_2' not in activities_df.columns:
        st.error("'count_degree_2' column not found in the DataFrame.")
        return  # Exit the function if the column doesn't exist

    # Big title with custom style
    st.title("Activities Recommendation")
    
    # Subheading with nice text
    st.write("Activities to Meet Mutual Friends")

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
            background-color: #0000FF;
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
    activities_df_new = activities_df[activities_df['count_degree_2'] > 0]
    activities_df_new = activities_df_new.sort_values(by='count_degree_2', ascending=False)
    
    # Display activities with the highest 2nd-degree connections first
    for _, row in activities_df_new.iterrows():
        count = row['count_degree_2']
        
        # Adjust for singular/plural usage
        people_word = "person" if count == 1 else "people"
        share_word = "shares" if count == 1 else "share"
        
        # Make activity name bold, blue, and larger font size
        activity_name = f"<span style='font-weight: bold; color: #0000FF; font-size: 22px;'>{row['activities']}</span>"
        
        # Construct the message
        message = f"Join {activity_name} to meet {count} new {people_word} that {share_word} a mutual friend."
        
        # Display the message with left-aligned text
        st.markdown(f"<div style='text-align: left;'>{message}</div>", unsafe_allow_html=True)

    # Add some space before the DataFrame
    st.markdown("<br>", unsafe_allow_html=True)

    # Display DataFrame with styling
    st.dataframe(activities_df.style.set_table_attributes('class="streamlit-table"'))

    # Back button to navigate to the previous page
    back_clicked = st.button("Back")
    if back_clicked:
        st.session_state.page = "student_landing_page"
