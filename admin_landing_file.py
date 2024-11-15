import streamlit as st
from custom_css_file import get_custom_css_page
from algorithm import network_map
from population_data_file import population_df, full_population_df
import networkx as nx
import pandas as pd
from itertools import combinations
import numpy as np

# Function to handle the admin landing page view
def get_admin_landing_page():
    get_custom_css_page(alignment="center", button_span="full")
    
    st.title("Admin Dashboard")
    st.markdown("<h3 style='text-align: left; color: #4A90E2;'>Network Map</h3>", unsafe_allow_html=True)
    network_map(population_df)

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
        st.markdown("<h3 style='text-align: left; color: #4A90E2;'>Students' Interests per Group</h3>", unsafe_allow_html=True)
        st.write(int_count_df)

        # Interpretation
        def get_groups_above_threshold(row, threshold=2):
            # Extract counts and filter by threshold
            counts = [int(count) for count in row.iloc[1:]]
            return [(i, count) for i, count in enumerate(counts) if count >= threshold]
        
        def format_event_details(interest, groups):
            total_count = sum(count for _, count in groups)
            group_text = " & ".join(f"group {i + 1}" for i, _ in groups)
            return f"<b style='color: #4A90E2;'>{interest.capitalize()} Event:</b> connecting {total_count} people from {group_text}"
        
        def get_participant_emails(df, interest, groups):
            emails = set()  # Use set to avoid duplicate emails
            for component, _ in groups:
                component_emails = df[(
                    df['component'] == component) & 
                    (df['interests'].apply(lambda x: interest in x))
                ]['0_degree'].apply(lambda x: f"{x}@falcon.bentley.edu")
                emails.update(component_emails)  # Adding to set to ensure uniqueness
            return emails
        
        # Main processing loop
        sentences = []
        for _, row in int_count_df.iterrows():  # changed interest_count_df to int_count_df
            interest = row['interest']
            groups = get_groups_above_threshold(row)
            
            if len(groups) > 1:
                # Add event description with capitalized event name
                event_detail = format_event_details(interest, groups)
                sentences.append(f"<div style='text-align: left; margin: 0;'>{event_detail}</div>")
                
                # Format and display emails with bullets
                email_list = get_participant_emails(df, interest, groups)
                if email_list:
                    email_text = "<ul style='margin: 0; padding-left: 20px;'>"  # Start unordered list with no margin
                    for email in email_list:
                        email_text += f"<li>{email}</li>"  # Add each email as a list item
                    email_text += "</ul>"  # End unordered list
                else:
                    email_text = "<p>No participants found for this event.</p>"

                # Add emails without extra empty lines
                sentences.append(f"<div style='text-align: left; margin: 0;'>{email_text}</div>")

        return int_count_df, sentences

    int_count_df, sentences = get_common_interests_table(full_population_df)

    # Display Suggestions with proper formatting (no empty lines)
    st.markdown("<h3 style='text-align: left; color: #4A90E2;'>Event Recommendations</h3>", unsafe_allow_html=True)
    for sentence in sentences:
        st.markdown(sentence, unsafe_allow_html=True)  # Render each sentence with HTML formatting
    
    # Optionally, add a button to go back to the login/signup page
    if st.button('Log out'):
        st.session_state.page = "login_signup_page"  # Ensure this part matches your session management system
