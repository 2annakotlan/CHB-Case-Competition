def get_profile_info_page(population_df):
    # Apply custom CSS with specified alignment and button span
    get_custom_css_page(alignment="left", button_span="auto") 

    # Format user's email prefix for the profile title
    email_prefix = st.session_state.user_email.split('@')[0]
    formatted_prefix = f"{email_prefix[0].upper()}. {email_prefix[1:].capitalize()}"
    st.title(f"{formatted_prefix}'s Profile") 
    
    # Collect user's 1st-degree connections
    selected_connections = st.text_input("Enter your friends (e.g., AKotlan, RMiller, SLogan, etc.)")
    
    # Predefined options for interests and activities from imported data files
    interest_options = interests
    activity_options = activities
    
    # Collect user's interests using a multi-select option without a default value
    selected_interests = st.multiselect("Select your interests", interest_options)
    
    # Collect user's activities using a multi-select option without a default value
    selected_activities = st.multiselect("Select your activities", activity_options)

    # Button to submit the profile information
    if st.button('Enter', use_container_width=False):
        # Format the input data
        formatted_connections = "{" + selected_connections.replace(" ", ";").replace(",", ";") + "}"
        formatted_activities = "{" + ";".join(selected_activities) + "}"
        formatted_interests = "{" + ";".join(selected_interests) + "}"
        
        if email_prefix in population_df["0_degree"].values:
            # Update the existing row in population_df (no reassignment needed)
            population_df.loc[population_df["0_degree"] == email_prefix, ["1_degree", "activities", "interests"]] = [
                formatted_connections,
                formatted_activities,
                formatted_interests]
        else:
            # Add a new row for the user (without reassigning population_df)
            new_row = {
                "0_degree": email_prefix,
                "1_degree": formatted_connections,
                "activities": formatted_activities,
                "interests": formatted_interests
            }
            # Here, we're modifying population_df by appending a new row
            population_df = pd.concat([population_df, pd.DataFrame([new_row])], ignore_index=True)
        
        # Save the updated population_df to session state
        st.session_state.population_df = population_df

        # Set the session state to navigate to the student landing page
        st.session_state.page = "student_landing_page"
