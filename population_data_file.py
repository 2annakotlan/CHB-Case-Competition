import pandas as pd
import numpy as np
data = {
    '0_degree': [
        'Alice', 'Bob', 'Charlie', 'Diana',
        'Emma', 'Frank', 'Grace', 'Henry',
        'Isabel', 'Jack', 'Kelly', 'Liam',
        'Maya', 'Noah', 'Olivia', 'Paul',
        'Quinn', 'Ryan', 'Sofia', 'Tyler',
        'Uma', 'Victor', 'Wendy', 'Xavier',
        'No', 'Liza', 'Karen', 'Ye',
        'Barbara', 'Kayleigh', 'Aideen'
    ],
    '1_degree': [
        {'Ivanka'},
        {'Alice', 'Diana'},
        {'Alice', 'Diana', 'Bob'},
        {'Alice', 'Bob'},
        {'Grace', 'Frank', 'Henry'},
        {'Emma', 'Grace', 'Henry'},
        {'Emma', 'Los', 'Isabel'},
        {'Frank', 'Grace', 'Jack'},
        {'Grace', 'Henry', 'Kelly'},
        {'Henry', 'Kelly', 'Liam'},
        {'Isabel', 'Jack', 'Maya'},
        {'Jack', 'Kelly', 'Noah'},
        {'Kelly', 'Liam', 'Olivia'},
        {'Maya', 'Olivia', 'Paul'},
        {'Maya', 'Noah', 'Quinn'},
        {'Noah', 'Olivia', 'Ryan'},
        {'Paul', 'Ryan', 'Sofia'},
        {'Quinn', 'Sofia', 'Tyler'},
        {'Ryan', 'Tyler', 'Uma'},
        {'Sofia', 'Uma', 'Victor'},
        {'Tyler', 'Victor', 'Wendy'},
        {'Uma', 'Wendy', 'Xavier'},
        {'Victor', 'Xavier', 'Quinn'},
        {'Wendy', 'Uma', 'Ryan'},
        {'Liza', 'Karen'},
        {'No', 'Karen'},
        {'No'},
        set(),
        {'Kayleigh', 'Aideen'},
        {'Aideen', 'Barbara'},
        {'Barbara', 'Kayleigh'}
    ],
    'interests': [
        {'Finance & Investment', 'Religious Identities'},
        {'Religious Identities', 'Finance & Investment'},
        {'Gender & Sexual Identities', 'Political, Legal, & Public Affairs'},
        {'Gender & Sexual Identities', 'Finance & Investment'},
        {'Games', 'Finance & Investment'},
        {'Religious Identities', 'Political, Legal, & Public Affairs'},
        {'Games', 'Social Impact & Community Development'},
        {'Finance & Investment', 'Political, Legal, & Public Affairs'},
        {'Social Impact & Community Development', 'Gender & Sexual Identities'},
        {'Social Impact & Community Development', 'Community Engagement & Leadership'},
        {'Community Engagement & Leadership', 'Cultural & Ethnic Identities'},
        {'Performing Arts', 'Games', 'Political, Legal, & Public Affairs'},
        {'Finance & Investment', 'Political, Legal, & Public Affairs'},
        {'Finance & Investment', 'Community Engagement & Leadership'},
        {'Finance & Investment', 'Finance & Investment'},
        {'Entrepreneurship & Business Strategy', 'Social Impact & Community Development'},
        {'Entrepreneurship & Business Strategy', 'Games'},
        {'Games', 'Sports & Fitness', 'Finance & Investment'},
        {'Political, Legal, & Public Affairs', 'Sports & Fitness'},
        {'Finance & Investment', 'Finance & Investment'},
        {'Political, Legal, & Public Affairs', 'Games'},
        {'Cultural & Ethnic Identities', 'Games'},
        {'Games', 'Political, Legal, & Public Affairs'},
        {'Cultural & Ethnic Identities', 'Games'},
        {'Games'},
        {'Entrepreneurship & Business Strategy'},
        {'Entrepreneurship & Business Strategy'},
        {'Finance & Investment'},
        {'Sports & Fitness'},
        {'Cultural & Ethnic Identities'},
        {'Finance & Investment'}
    ],
    'activities': [
        {'Sigma Chi', 'Black United Body'},
        {'South Asian Student Association', 'Cru Bentley'},
        {'Black United Body', 'Sigma Chi'},
        {'South Asian Student Association', 'Bentley Active Minds'},
        {'Bentley Active Minds', 'Sigma Chi'},
        {'Cheer', 'Cru Bentley'},
        {'South Asian Student Association', 'Cru Bentley'},
        {'International Student Association', 'Cheer'},
        {'Bentley Active Minds', 'Her Campus'},
        {'Black United Body', 'Her Campus'},
        {'Bentley Active Minds', 'Cheer'},
        {'Sigma Gamma Delta', 'Cheer'},
        {'South Asian Student Association', 'Bentley Skating Club'},
        {'Cru Bentley', 'South Asian Student Association'},
        {'Sigma Chi', 'International Student Association'},
        {'Bentley Skating Club', 'Cru Bentley'},
        {'Sigma Chi', 'Sigma Gamma Delta'},
        {'Sigma Gamma Delta', 'Bentley Skating Club'},
        {'Sigma Chi', 'Bentley Chess Club'},
        {'Esports', 'Bentley Chess Club'},
        {'Esports', 'International Student Association'},
        {'Hillel', 'Cheer'},
        {'Sigma Gamma Delta', 'Hillel'},
        {'Hillel', 'South Asian Student Association'},
        {'Cheer', 'Bentley Active Minds'},
        {'South Asian Student Association', 'Bentley Active Minds'},
        {'Hillel', 'Bentley Active Minds'},
        set(),
        {'Sigma Gamma Delta'},
        {'Hillel'},
        set()
    ]
}

population_df = pd.DataFrame(data)
population_df['match'] = np.ones(len(population_df))

# FULL DATA
import networkx as nx
def get_nth_degree(df, n):
    df[f'{n}_degree'] = None  # new column for nth-degree connections
    for index, row in df.iterrows():  # for every person in the dataframe...
        previous_degree = row[f'{n-1}_degree']  # get list of their previous-degree connections
        all_previous_degrees = set()  # get list of ALL previous degree connections
        for i in range(0, n): 
            all_previous_degrees.update(row[f'{i}_degree'])
        
        n_degree_set = set()  # initialize set to store unique nth-degree values
        for i in previous_degree:  # for each person in the previous-degree connections list...
            matching_row = df[df['0_degree'] == i]  # find the row where the 'name' matches the current previous-degree connection
            if not matching_row.empty:  # if that person exists in the list...
                # Extract their nth degree connections (excluding all_previous_degrees), but also remove their own 0_degree connection if present
                nth_degree = set(matching_row[f'{n-1}_degree'].values[0]) - all_previous_degrees
                nth_degree.discard(row['0_degree'])  # Make sure the person doesn't add their own 0_degree to their nth degree
                n_degree_set.update(nth_degree)

        # Save to dataframe as a set of unique connections
        df.at[index, f'{n}_degree'] = n_degree_set

    # Remove nth-degree connections that don't exist in the dataset
    for index, row in df.iterrows(): 
        nth_degree_names = row[f'{n}_degree']
        valid_names = nth_degree_names & set(df['0_degree'])
        df.at[index, f'{n}_degree'] = valid_names

    return df

def get_full_df(df):
    n = 2  # Start with degree 2 since degree 1 is assumed to be already populated
    while True:
        df = get_nth_degree(df, n)
        
        # Check if all entries in the new degree column are empty sets
        if df[f'{n}_degree'].apply(lambda x: len(x) == 0).all():
            # Drop the current n_degree column if it has all empty sets
            df = df.drop(columns=[f'{n}_degree'])
            break
        
        n += 1

    G = nx.Graph()

    # Add nodes and edges based on the dataframe
    for _, row in df.iterrows():
        G.add_node(row['0_degree'])
        for connection in row['1_degree']:
            G.add_edge(row['0_degree'], connection)

    # Get all connected components
    components = list(nx.connected_components(G))

    # Create a dictionary to map each node to its component index
    node_to_component = {}
    for index, component in enumerate(components):
        for node in component:
            node_to_component[node] = index

    # Add a new column to the dataframe with the component index
    df['component'] = df['0_degree'].map(node_to_component)

    return df

full_population_df = get_full_df(population_df)

comp_num = full_population_df['component'].nunique()

degree_columns = [col for col in full_population_df.columns if '_degree' in col]

# Step 2: Find the last non-empty column for each row
def find_last_non_empty(row):
    for col in reversed(degree_columns):  # Iterate over degree columns in reverse
        if row[col] != set():  # Check if the column value is not an empty set
            return int(col.split('_')[0])  # Extract the degree number (e.g., "1" from "1_degree")
    return 0  # Return 0 if all are empty

# Apply the function to each row
full_population_df['last_non_empty_degree'] = full_population_df.apply(find_last_non_empty, axis=1)

# Step 3: Calculate the average of the last non-empty degree
average_last_degree = full_population_df['last_non_empty_degree'].mean()

