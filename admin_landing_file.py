import streamlit as st
from custom_css_file import get_custom_css_page
from algorithm import network_map
from population_data_file import population_df, full_population_df

# Function to handle the admin landing page view
def get_admin_landing_page():
    get_custom_css_page(alignment="center", button_span="auto")
    
    st.title("Admin Dashboard")
    st.markdown("<h3 style='text-align: center; color: #4A90E2;'>Network Map</h3>", unsafe_allow_html=True)
    network_map(population_df)

    import networkx as nx
    import pandas as pd
    from itertools import combinations
    import numpy as np

    # Function to find common interests and interpret connections
    def get_common_interests_table(df):
        # Explode the interests and count occurrences by component
        comp_int_expanded_df = df.explode('interests')[['component', 'interests']]
        comp_int_df = comp_int_expanded_df.groupby(['component', 'interests']).size().reset_index(name='count')
        comp_int_df = comp_int_df.sort_values(by=['component', 'count'], ascending=[True, False]).reset_index(drop=True)
    
        # Pivot table to show interest counts per component
        int_count_df = comp_int_df.pivot_table(
            index='interests',
            columns='component',
            values='count',
            fill_value=0
        ).reset_index()
    
        int_count_df.columns = ['interest'] + [f'Group {i}' for i in range(len(int_count_df.columns) - 1)]
    
        # Round the values to the nearest whole number
        int_count_df.iloc[:, 1:] = int_count_df.iloc[:, 1:].round(0)
        
        # Convert the rounded values to integers
        int_count_df.iloc[:, 1:] = int_count_df.iloc[:, 1:].astype(int)

        return int_count_df
    
    # Get the common interest table and process it
    int_count_df = get_common_interests_table(full_population_df)
    
    # Display the final table
    st.markdown("<h3 style='text-align: center; color: #4A90E2;'>Students' Interests per Group</h3>", unsafe_allow_html=True)
    st.table(int_count_df)
    
    # Event recommendations interpretation
    sentences = []
    for _, row in int_count_df.iterrows():  # for each interest...
        interest = row['interest']  # get the interest
        counts = [int(row[col]) for col in row.index[1:]]  # count of people per component
        counts_above_threshold = [(i, count) for i, count in enumerate(counts) if count >= 2] # count of people per component filtered by threshold

        if len(counts_above_threshold) > 1:  # if there is more than 1 group...
            if counts_above_threshold:  # for groups above the threshold...
                total_count = sum(count for _, count in counts_above_threshold)  # total count of people
                group_details = ", ".join(f"group {i} ({count} {'people' if count > 1 else 'person'})" for i, count in counts_above_threshold)  # count of people per group
                sentences.append(f"{interest.capitalize()} event: connects {total_count} people from {group_details}")  # sentence

                all_names = []  # names of people in each component with this interest
                for component, _ in counts_above_threshold:  # for each component...
                    names = full_population_df[(full_population_df['component'] == component) & (full_population_df['interests'].apply(lambda x: interest in x))]['0_degree'].tolist()  # get names
                    all_names.extend(names)  # append to list
                sentences.append(f"  Emails: {', '.join(all_names)}")
                sentences.append("")

    # Display Event Recommendations
    st.markdown("<h3 style='text-align: left; color: #4A90E2;'>Event Recommendations</h3>", unsafe_allow_html=True)
    st.text("\n".join(sentences))

    # Optionally, add a button to go back to the login/signup page
    if st.button('Log out'):
        st.session_state.page = "login_signup_page"
