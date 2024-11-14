
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
