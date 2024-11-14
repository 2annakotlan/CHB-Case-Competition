import pandas as pd
from collections import Counter

def get_activities(df, name):
    # Determine the number of degree columns (excluding the first degree column '0_degree')
    n = sum('_degree' in col for col in df.columns) - 1  # Assuming '0_degree' is the first degree column
    
    # Initialize a list to store unique activities
    unique_activities = pd.Series([item for sublist in df['activities'] for item in sublist]).unique()
    
    # Initialize the data dictionary for the new DataFrame
    data = {'activities': unique_activities}

    # Initialize counts for each degree (starting from 1st degree)
    for count in range(1, n + 1):
        data[f'count_degree_{count}'] = [0] * len(unique_activities)

    # Get the second-degree, third-degree, etc., connections for the specified name
    for i in range(1, n + 1):
        degree_column = f'{i}_degree'
        
        # Get the nth-degree individuals for the specified name
        degree_connections = df[df['0_degree'] == name][degree_column].tolist()
        
        # Flatten the list of nth-degree connections if necessary
        degree_connections_flat = []
        for items in degree_connections:
            if isinstance(items, set):
                degree_connections_flat.extend(items)
            elif isinstance(items, str):
                degree_connections_flat.append(items)

        # Collect all activities for the nth-degree individuals
        all_activities = []
        for connection in degree_connections_flat:
            activities = df[df['0_degree'] == connection]['activities'].tolist()
            for activity in activities:
                if isinstance(activity, set):
                    all_activities.extend(activity)  # Flatten set activities into the list
                else:
                    all_activities.append(activity)  # Append individual activities directly
        
        # Count activities and update the counts in the dataframe for the current degree level
        activity_counts = Counter(all_activities)
        for activity, count in activity_counts.items():
            if activity in unique_activities:
                activity_index = list(unique_activities).index(activity)
                data[f'count_degree_{i}'][activity_index] += count

    # Create the activities DataFrame
    activities_df = pd.DataFrame(data)

    # Drop columns where all entries are empty sets
    for i in range(1, n + 1):
        degree_column = f'{i}_degree'
        
        # Check if all entries in the degree column are empty sets
        if activities_df[f'count_degree_{i}'].apply(lambda x: x == 0).all():
            # Drop the column if it has all zeros (i.e., no activities for that degree)
            activities_df = activities_df.drop(columns=[f'count_degree_{i}'])

    # Return the DataFrame with activities and counts
    return activities_df


