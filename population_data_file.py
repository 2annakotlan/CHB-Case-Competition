# ORIGIONAL DATA
import pandas as pd

population_data = {
      "0_degree": ["e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8", "e9", "e10", "e11", "e12", "e13", "e14", "e15", "e16", "e17", "e18", "e19", "e20", "e21", "e22", "e23", "e24", "e25", "e26", "e27", "e28", "e29", "e30", "e31", "e32", "e33", "e34", "e35", "e36", "e37", "e38", "e39", "e40", "e41", "e42", "e43", "e44", "e45", "e46", "e47", "e48", "e49", "e50", "e51", "e52", "e53", "e54", "e55", "e56", "e57", "e58", "e59", "e60", "e61", "e62", "e63", "e64", "e65", "e66", "e67", "e68", "e69", "e70", "e71", "e72", "e73", "e74", "e75", "e76", "e77", "e78", "e79", "e80", "e81", "e82", "e83", "e84", "e85", "e86", "e87", "e88", "e89", "e90", "e91", "e92", "e93", "e94", "e95", "e96", "e97", "e98", "e99", "e100", "stest"],
      "1_degree": [{"e3", "e45", "e22"}, {"e12", "e89"}, {"e8", "e56", "e99", "e17"}, {"e100", "e102", "e103"}, {"e20", "e53", "e11"}, {"e25", "e7", "e70"}, {"e50", "e33"}, {"e40", "e29", "e88", "e77"}, {"e9"}, {"e31", "e62", "e51"}, {"e5", "e13"}, {"e6", "e28", "e91"}, {"e18", "e34"}, {"e81", "e2", "e67"}, {"e41", "e75"}, {"e4", "e55", "e49"}, {"e101"}, {"e46", "e11"}, {"e21", "e19", "e90"}, {"e37", "e71", "e63"}, {"e27", "e69", "e1"}, {"e38", "e59"}, {"e15", "e60"}, {"e72", "e76", "e3"}, {"e32", "e78"}, {"e42", "e34", "e24"}, {"e16"}, {"e26", "e48"}, {"e14", "e30"}, {"e57"}, {"e67", "e82"}, {"e39"}, {"e74", "e10", "e23"}, {"e58", "e61", "e79"}, {"e36"}, {"e43", "e73"}, {"e68", "e41"}, {"e44"}, {"e5", "e62", "e87"}, {"e66", "e70"}, {"e21", "e9", "e51"}, {"e75", "e12"}, {"e64", "e52"}, {"e16", "e40"}, set(), {"e83", "e44"}, {"e7", "e15", "e77"}, {"e17", "e50"}, {"e10", "e92", "e13"}, {"e84"}, {"e61", "e63"}, {"e80", "e3"}, {"e47", "e93"}, {"e49"}, {"e22", "e27"}, {"e56", "e5"}, {"e74"}, {"e71", "e8"}, {"e29"}, {"e54", "e39", "e14"}, {"e20", "e83"}, {"e90"}, {"e25"}, {"e63", "e56"}, {"e67"}, {"e33", "e13"}, {"e49", "e9"}, set(), {"e60", "e2"}, {"e50"}, {"e43", "e35", "e51"}, {"e13", "e34"}, {"e48", "e92"}, {"e29"}, {"e78", "e50"}, {"e84", "e27"}, {"e32"}, {"e65"}, {"e24", "e58", "e7"}, {"e88"}, {"e31", "e82"}, {"e1", "e46", "e59"}, {"e41", "e56"}, set(), {"e61", "e25"}, {"e78"}, {"e11", "e20"}, {"e6", "e10", "e51"}, {"e32"}, {"e69", "e44"}, {"e33"}, {"e77", "e18"}, {"e60", "e17"}, {"e74", "e16"}, {"e79", "e13"}, {"e2", "e45", "e72"}, {"e21", "e38"}, {"e49", "e56"}, {"e61", "e9"}, {"e75", "e92"}, {"e1", "e3", "e7", "e13", "e21", "e44"}],
      "activities": [{"Adamian Law Club", "Alpha Kappa Psi", "Bentley Consulting Group"}, {"Bentley Entrepreneurship Society"}, {"Bentley Investment Group", "Bentley Leadership Society"}, {"Bentley Marketing Association", "Bentley Microfinance Group", "Bentley Non-Profit Society"}, {"Bentley Open Market Committee"}, {"Bentley Real Estate Group"}, set(), {"Delta Sigma Pi", "Gamma Iota Sigma"}, {"Information Systems Audit Control Association", "Leading Women of Tomorrow"}, {"Sustainable Investment Group"}, set(), {"Bentley Alternative Investments Group", "Bentley Blockchain Association"}, {"Bentley Economic-Finance Society", "Bentley Investment Banking Club"}, {"Bentley Philosophy Club"}, {"Model United Nations", "National Association of Black Accountants", "Scholars of Finance"}, {"Students for Sustainable Business"}, {"Alpha Psi Omega"}, set(), set(), {"Bentley Chamber Orchestra", "Bentley Climbing Club"}, {"Bentley Film Company", "Bentley Music Collective"}, {"Bentley Photography Association"}, {"Bentley Tennis Club", "Bentley Student Gaming Organization"}, {"CRAZE"}, {"Fashion Association at Bentley"}, {"Golf Association"}, {"Fitness Club", "Kosmos"}, {"Literary Society", "Momentum"}, {"Off the Clock", "Project Creative Industries"}, {"Ski & Snowboard Club", "Spikeball Club"}, set(), {"Bentley Painter's Organization"}, {"Bentley Running Club", "Bentley Skating Club"}, {"Bentley Streetwear Society"}, set(), {"Jazz Band"}, {"Student-Athlete Advisory Committee", "Sports Business Association"}, {"Climbing Club", "Cheer"}, {"Dance", "Equestrian"}, {"Esports", "Men's and Women's Hockey"}, {"Men's and Women's Rugby", "Sailing"}, {"Triathlon"}, {"Men's and Women's Ultimate", "Men's and Women's Volleyball"}, {"Allocation & Internal Audit Committee"}, {"Alpha Phi Omega", "Bentley Democrats"}, {"Best Buddies International"}, {"Campus Activities Board"}, {"Class Cabinets", "Circle K"}, set(), set(), {"The Vanguard"}, {"WBTY", "Pinky Swear PACK"}, {"Alpha Epsilon Pi", "Alpha Gamma Pi", "Alpha Phi"}, {"Bentley Interfraternity Council", "Bentley Panhellenic Council"}, {"Delta Kappa Epsilon", "Gamma Phi Beta", "Greek Activities Council"}, {"Kappa Delta", "Kappa Sigma"}, {"Phi Sigma Sigma", "Sigma Chi", "Sigma Gamma Delta", "Sigma Pi"}, {"Delta Sigma Iota"}, set(), {"Bentley Asian Students' Association", "Bentley Association of Chinese Students"}, {"Bentley Catholic Association", "Black United Body"}, {"Brazilian Students Society", "Cape Verdean Student Association"}, {"Caribbean Ancestry Student Association", "Cru Bentley"}, {"Hillel"}, {"International Student Association"}, {"Identity and Advocacy, Sexuality, Gender Equality"}, {"La Cultura Latina", "La Societa Italiana di Bentley"}, {"People Respecting Individuality & Diversity through Education"}, {"Philippine United Student Organization", "South Asian Student Association"}, {"Student Advocating Gender Equality", "Vietnamese Student Association"}, {"Young Arab Leaders Association", "Bentley Active Minds"}, {"Eastern European Student Association", "Ghanaian Ancestry Student Association"}, {"Thai Student Association", "Albanian Student Organization"}, set(), {"Africana Student Association", "Armenian Student Association"}, {"Bentley Asian Students' Association", "Bentley Association of Chinese Students"}, {"Bentley Catholic Association", "Black United Body"}, {"Brazilian Students Society", "Cape Verdean Student Association"}, {"Caribbean Ancestry Student Association", "Cru Bentley"}, {"Hillel"}, {"International Student Association"}, {"Identity and Advocacy, Sexuality, Gender Equality"}, {"La Cultura Latina", "La Societa Italiana di Bentley"}, {"People Respecting Individuality & Diversity through Education"}, {"Philippine United Student Organization", "South Asian Student Association"}, set(), set(), {"Fitness Club", "Kosmos"}, {"Literary Society", "Momentum"}, {"Off the Clock", "Project Creative Industries"}, {"Ski & Snowboard Club", "Spikeball Club"}, {"Bentley Chess Club", "Bentley Irish Dance Club"}, {"Bentley Painter's Organization"}, {"Bentley Running Club", "Bentley Skating Club"}, {"Bentley Streetwear Society"}, {"Her Campus"}, {"Jazz Band"}, {"Student-Athlete Advisory Committee", "Sports Business Association"}, {"Climbing Club", "Cheer"}, {"Dance", "Equestrian"}, {"STEM", "Games", "Performing Arts"}],
      "interests": [{"Finance & Investment"}, {"Entrepreneurship & Business Strategy"}, {"Political, Legal, & Public Affairs"}, {"Social Impact & Community Development"}, {"Community Engagement & Leadership"}, {"STEM"}, {"Visual Arts & Media Production"}, {"Performing Arts"}, {"Sports & Fitness"}, {"Games"}, {"Cultural & Ethnic Identities"}, {"Religious Identities"}, {"Gender & Sexual Identities"}, {"Finance & Investment", "Entrepreneurship & Business Strategy"}, {"Finance & Investment", "Political, Legal, & Public Affairs"}, {"Finance & Investment", "Social Impact & Community Development"}, {"Finance & Investment", "STEM"}, {"Finance & Investment", "Visual Arts & Media Production"}, {"Finance & Investment", "Performing Arts"}, {"Finance & Investment", "Sports & Fitness"}, {"Finance & Investment", "Games"}, {"Finance & Investment", "Cultural & Ethnic Identities"}, {"Finance & Investment", "Religious Identities"}, {"Finance & Investment", "Gender & Sexual Identities"}, {"Entrepreneurship & Business Strategy", "Political, Legal, & Public Affairs"}, {"Entrepreneurship & Business Strategy", "Social Impact & Community Development"}, {"Entrepreneurship & Business Strategy", "STEM"}, {"Entrepreneurship & Business Strategy", "Visual Arts & Media Production"}, {"Entrepreneurship & Business Strategy", "Performing Arts"}, {"Entrepreneurship & Business Strategy", "Sports & Fitness"}, {"Entrepreneurship & Business Strategy", "Games"}, {"Entrepreneurship & Business Strategy", "Cultural & Ethnic Identities"}, {"Entrepreneurship & Business Strategy", "Religious Identities"}, {"Entrepreneurship & Business Strategy", "Gender & Sexual Identities"}, {"Political, Legal, & Public Affairs", "Social Impact & Community Development"}, {"Political, Legal, & Public Affairs", "STEM"}, {"Political, Legal, & Public Affairs", "Visual Arts & Media Production"}, {"Political, Legal, & Public Affairs", "Performing Arts"}, {"Political, Legal, & Public Affairs", "Sports & Fitness"}, {"Political, Legal, & Public Affairs", "Games"}, {"Political, Legal, & Public Affairs", "Cultural & Ethnic Identities"}, {"Political, Legal, & Public Affairs", "Religious Identities"}, {"Political, Legal, & Public Affairs", "Gender & Sexual Identities"}, {"Social Impact & Community Development", "STEM"}, {"Social Impact & Community Development", "Visual Arts & Media Production"}, {"Social Impact & Community Development", "Performing Arts"}, {"Social Impact & Community Development", "Sports & Fitness"}, {"Social Impact & Community Development", "Games"}, {"Social Impact & Community Development", "Cultural & Ethnic Identities"}, {"Social Impact & Community Development", "Religious Identities"}, {"Social Impact & Community Development", "Gender & Sexual Identities"}, {"Community Engagement & Leadership", "STEM"}, {"Community Engagement & Leadership", "Visual Arts & Media Production"}, {"Community Engagement & Leadership", "Performing Arts"}, {"Community Engagement & Leadership", "Sports & Fitness"}, {"Community Engagement & Leadership", "Games"}, {"Community Engagement & Leadership", "Cultural & Ethnic Identities"}, {"Community Engagement & Leadership", "Religious Identities"}, {"Community Engagement & Leadership", "Gender & Sexual Identities"}, {"STEM", "Visual Arts & Media Production"}, {"STEM", "Performing Arts"}, {"STEM", "Sports & Fitness"}, {"STEM", "Games"}, {"STEM", "Cultural & Ethnic Identities"}, {"STEM", "Religious Identities"}, {"STEM", "Gender & Sexual Identities"}, {"Visual Arts & Media Production", "Performing Arts"}, {"Visual Arts & Media Production", "Sports & Fitness"}, {"Visual Arts & Media Production", "Games"}, {"Visual Arts & Media Production", "Cultural & Ethnic Identities"}, {"Visual Arts & Media Production", "Religious Identities"}, {"Visual Arts & Media Production", "Gender & Sexual Identities"}, {"Performing Arts", "Sports & Fitness"}, {"Performing Arts", "Games"}, {"Performing Arts", "Cultural & Ethnic Identities"}, {"Performing Arts", "Religious Identities"}, {"Performing Arts", "Gender & Sexual Identities"}, {"Sports & Fitness", "Games"}, {"Sports & Fitness", "Cultural & Ethnic Identities"}, {"Sports & Fitness", "Religious Identities"}, {"Sports & Fitness", "Gender & Sexual Identities"}, {"Games", "Cultural & Ethnic Identities"}, {"Games", "Religious Identities"}, {"Games", "Gender & Sexual Identities"}, {"Cultural & Ethnic Identities", "Religious Identities"}, {"Cultural & Ethnic Identities", "Gender & Sexual Identities"}, {"Religious Identities", "Gender & Sexual Identities"}, {"Finance & Investment", "Entrepreneurship & Business Strategy", "Political, Legal, & Public Affairs"}, {"Finance & Investment", "Entrepreneurship & Business Strategy", "Social Impact & Community Development"}, {"Finance & Investment", "Entrepreneurship & Business Strategy", "STEM"}, {"Finance & Investment", "Entrepreneurship & Business Strategy", "Visual Arts & Media Production"}, {"Finance & Investment", "Entrepreneurship & Business Strategy", "Performing Arts"}, {"Finance & Investment", "Entrepreneurship & Business Strategy", "Sports & Fitness"}, {"Finance & Investment", "Entrepreneurship & Business Strategy", "Games"}, {"Finance & Investment", "Entrepreneurship & Business Strategy", "Cultural & Ethnic Identities"}, {"Finance & Investment", "Entrepreneurship & Business Strategy", "Religious Identities"}, {"Finance & Investment", "Entrepreneurship & Business Strategy", "Gender & Sexual Identities"}, {"Finance & Investment", "Political, Legal, & Public Affairs", "Social Impact & Community Development"}, {"Finance & Investment", "Political, Legal, & Public Affairs", "STEM"}, {"Finance & Investment", "Political, Legal, & Public Affairs", "Visual Arts & Media Production"}, {"DECA", "Tamid", "Cheer"}]
    }

population_df = pd.DataFrame(population_data)

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

