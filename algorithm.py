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


import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go

def network_map(df):
    # CREATE THE NETWORK MAP
    G = nx.Graph()  # initialize an empty undirected graph

    for _, row in df.iterrows():  # for each row in the dataframe...
        G.add_node(row['0_degree'])  # add a node for the person
        for connection in row['1_degree']:  # for each of their known connections...
            G.add_edge(row['0_degree'], connection)  # add an edge between the person and each connection

    # FORMAT THE NETWORK MAP
    # Connected Components
    components = list(nx.connected_components(G))  # get all connected components
    component_sizes = {i: len(component) for i, component in enumerate(components)}  # store the size of each component

    pos = {}  # initialize the position dictionary for all nodes
    offset_x = 0  # initialize the offset variable

    # Creating circular shape for components
    for i, component in enumerate(components):  # for each component...
        radius = component_sizes[i]  # set radius based on component size
        angles = np.linspace(0, 2 * np.pi, len(component), endpoint=False)  # angles for circular positioning

        component_pos = {
            node: (radius * np.cos(angle), radius * np.sin(angle))  # calculate (x, y) based on angle and radius
            for node, angle in zip(component, angles)} # assign a unique angle to each node in the component

        # Apply an offset to shift components to the right
        if i > 0:
            prev_max_x = max(pos[node][0] for node in components[i - 1]) # find the maximum x-coordinate from the previous component
            offset_x = prev_max_x + radius + 10 # sum of maximum x-coordinate from the previous component + radius
            component_pos = {node: (x + offset_x, y) for node, (x, y) in component_pos.items()} # shift the current component by the offset
        pos.update(component_pos) # update positions with the component's offset positions

    # Display the graph with components labeled
    plt.figure(figsize=(10, 10))
    nx.draw(G, pos=pos, with_labels=True, node_color='lightblue', node_size=400, font_size=9, font_weight='bold', edge_color='gray', width=1)

    # Adding component labels
    for i, component in enumerate(components):
        # Find the average position of the component for the label placement
        center_x = np.mean([pos[node][0] for node in component])
        center_y = np.mean([pos[node][1] for node in component])

        # Label the component with its index
        plt.text(center_x, center_y, i, fontsize=8, ha='center', va='center', fontweight='bold', color='black')

    plt.axis('equal')  # components are perfect circles
    plt.show()

# Calling Function
network_map(df)





