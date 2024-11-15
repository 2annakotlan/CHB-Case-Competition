# ORIGIONAL DATA
import pandas as pd

zero_degree = ["e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8", "e9", "e10", "e11", "e12", "e13", "e14", "e15", "e16", "e17", "e18", "e19", "e20", "e21", "e22", "e23", "e24", "e25", "e26", "e27", "e28", "e29", "e30", "e31", "e32", "e33", "e34", "e35", "e36", "e37", "e38", "e39", "e40", "e41", "e42", "e43", "e44", "e45", "e46", "e47", "e48", "e49", "e50", "e51", "e52", "e53", "e54", "e55", "e56", "e57", "e58", "e59", "e60", "e61", "e62", "e63", "e64", "e65", "e66", "e67", "e68", "e69", "e70", "e71", "e72", "e73", "e74", "e75", "e76", "e77", "e78", "e79", "e80", "e81", "e82", "e83", "e84", "e85", "e86", "e87", "e88", "e89", "e90", "e91", "e92", "e93", "e94", "e95", "e96", "e97", "e98", "e99", "e100", "stest"]
one_degree = [{"e3", "e2", "e4"}, {"e1", "e5"}, {"e1", "e4", "e5"}, {"e1", "e3", "e5"}, {"31", "32", "e3"}, {"e25", "e7", "e70"}, {"e50", "e33"}, {"e40", "e29", "e88", "e77"}, {"e9"}, {"e31", "e62", "e51"}, {"e5", "e13"}, {"e6", "e28", "e91"}, {"e18", "e34"}, {"e81", "e2", "e67"}, {"e41", "e75"}, {"e4", "e55", "e49"}, {"e101"}, {"e46", "e11"}, {"e21", "e19", "e90"}, {"e37", "e71", "e63"}, {"e27", "e69", "e1"}, {"e38", "e59"}, {"e15", "e60"}, {"e72", "e76", "e3"}, {"e32", "e78"}, {"e42", "e34", "e24"}, {"e16"}, {"e26", "e48"}, {"e14", "e30"}, {"e57"}, {"e67", "e82"}, {"e39"}, {"e74", "e10", "e23"}, {"e58", "e61", "e79"}, {"e36"}, {"e43", "e73"}, {"e68", "e41"}, {"e44"}, {"e5", "e62", "e87"}, {"e66", "e70"}, {"e21", "e9", "e51"}, {"e75", "e12"}, {"e64", "e52"}, {"e16", "e40"}, set(), {"e83", "e44"}, {"e7", "e15", "e77"}, {"e17", "e50"}, {"e10", "e92", "e13"}, {"e84"}, {"e61", "e63"}, {"e80", "e3"}, {"e47", "e93"}, {"e49"}, {"e22", "e27"}, {"e56", "e5"}, {"e74"}, {"e71", "e8"}, {"e29"}, {"e54", "e39", "e14"}, {"e20", "e83"}, {"e90"}, {"e25"}, {"e63", "e56"}, {"e67"}, {"e33", "e13"}, {"e49", "e9"}, set(), {"e60", "e2"}, {"e50"}, {"e43", "e35", "e51"}, {"e13", "e34"}, {"e48", "e92"}, {"e29"}, {"e78", "e50"}, {"e84", "e27"}, {"e32"}, {"e65"}, {"e24", "e58", "e7"}, {"e88"}, {"e31", "e82"}, {"e1", "e46", "e59"}, {"e41", "e56"}, set(), {"e61", "e25"}, {"e78"}, {"e11", "e20"}, {"e6", "e10", "e51"}, {"e32"}, {"e69", "e44"}, {"e33"}, {"e77", "e18"}, {"e60", "e17"}, {"e74", "e16"}, {"e79", "e13"}, {"e2", "e45", "e72"}, {"e21", "e38"}, {"e49", "e56"}, {"e61", "e9"}, {"e75", "e92"}, {"e1", "e3", "e7", "e13", "e21", "e44"}]
activities = [{"Adamian Law Club", "Alpha Kappa Psi", "Bentley Consulting Group"}, {"Bentley Entrepreneurship Society"}, {"Bentley Investment Group", "Bentley Leadership Society"}, {"Bentley Marketing Association", "Bentley Microfinance Group", "Bentley Non-Profit Society"}, {"Bentley Open Market Committee"}, {"Bentley Real Estate Group"}, set(), {"Delta Sigma Pi", "Gamma Iota Sigma"}, {"Information Systems Audit Control Association", "Leading Women of Tomorrow"}, {"Sustainable Investment Group"}, set(), {"Bentley Alternative Investments Group", "Bentley Blockchain Association"}, {"Bentley Economic-Finance Society", "Bentley Investment Banking Club"}, {"Bentley Philosophy Club"}, {"Model United Nations", "National Association of Black Accountants", "Scholars of Finance"}, {"Students for Sustainable Business"}, {"Alpha Psi Omega"}, set(), set(), {"Bentley Chamber Orchestra", "Bentley Climbing Club"}, {"Bentley Film Company", "Bentley Music Collective"}, {"Bentley Photography Association"}, {"Bentley Tennis Club", "Bentley Student Gaming Organization"}, {"CRAZE"}, {"Fashion Association at Bentley"}, {"Golf Association"}, {"Fitness Club", "Kosmos"}, {"Literary Society", "Momentum"}, {"Off the Clock", "Project Creative Industries"}, {"Ski & Snowboard Club", "Spikeball Club"}, set(), {"Bentley Painter's Organization"}, {"Bentley Running Club", "Bentley Skating Club"}, {"Bentley Streetwear Society"}, set(), {"Jazz Band"}, {"Student-Athlete Advisory Committee", "Sports Business Association"}, {"Climbing Club", "Cheer"}, {"Dance", "Equestrian"}, {"Esports", "Men's and Women's Hockey"}, {"Men's and Women's Rugby", "Sailing"}, {"Triathlon"}, {"Men's and Women's Ultimate", "Men's and Women's Volleyball"}, {"Allocation & Internal Audit Committee"}, {"Alpha Phi Omega", "Bentley Democrats"}, {"Best Buddies International"}, {"Campus Activities Board"}, {"Class Cabinets", "Circle K"}, set(), set(), {"The Vanguard"}, {"WBTY", "Pinky Swear PACK"}, {"Alpha Epsilon Pi", "Alpha Gamma Pi", "Alpha Phi"}, {"Bentley Interfraternity Council", "Bentley Panhellenic Council"}, {"Delta Kappa Epsilon", "Gamma Phi Beta", "Greek Activities Council"}, {"Kappa Delta", "Kappa Sigma"}, {"Phi Sigma Sigma", "Sigma Chi", "Sigma Gamma Delta", "Sigma Pi"}, {"Delta Sigma Iota"}, set(), {"Bentley Asian Students' Association", "Bentley Association of Chinese Students"}, {"Bentley Catholic Association", "Black United Body"}, {"Brazilian Students Society", "Cape Verdean Student Association"}, {"Caribbean Ancestry Student Association", "Cru Bentley"}, {"Hillel"}, {"International Student Association"}, {"Identity and Advocacy, Sexuality, Gender Equality"}, {"La Cultura Latina", "La Societa Italiana di Bentley"}, {"People Respecting Individuality & Diversity through Education"}, {"Philippine United Student Organization", "South Asian Student Association"}, set(), set(), {"Fitness Club", "Kosmos"}, {"Literary Society", "Momentum"}, {"Off the Clock", "Project Creative Industries"}, {"Ski & Snowboard Club", "Spikeball Club"}, {"Bentley Chess Club", "Bentley Irish Dance Club"}, {"Bentley Painter's Organization"}, {"Bentley Running Club", "Bentley Skating Club"}, {"Bentley Streetwear Society"}, {"Her Campus"}, {"Jazz Band"}, {"Student-Athlete Advisory Committee", "Sports Business Association"}, {"Climbing Club", "Cheer"}, {"Dance", "Equestrian"}, {"Esports", "Men's and Women's Hockey"}, {"Men's and Women's Rugby", "Sailing"}, {"Triathlon"}, {"Men's and Women's Ultimate", "Men's and Women's Volleyball"}, {"Allocation & Internal Audit Committee"}, {"Alpha Phi Omega", "Bentley Democrats"}, {"Best Buddies International"}, {"Campus Activities Board"}, {"Class Cabinets", "Circle K"}, set(), {"The Vanguard"}, {"WBTY", "Pinky Swear PACK"}, {"Alpha Epsilon Pi", "Alpha Gamma Pi", "Alpha Phi"}, {"Bentley Interfraternity Council", "Bentley Panhellenic Council"}, {"Delta Kappa Epsilon", "Gamma Phi Beta", "Greek Activities Council"}, {"Kappa Delta", "Kappa Sigma"}, {"Phi Sigma Sigma", "Sigma Chi", "Sigma Gamma Delta", "Sigma Pi"}, {"Delta Sigma Iota"}]
interests = [{"Artificial Intelligence", "Data Science"}, {"Climate Change", "Environmental Protection"}, {"Economic Policy", "International Affairs"}, {"Cryptography", "Network Security"}, {"Corporate Finance", "Private Equity"}, {"Supply Chain Management", "Operations"}, {"Theater", "Stage Production"}, {"Event Planning", "Marketing Communications"}, {"Investment Banking", "Financial Advisory"}, {"Real Estate Investment", "Asset Management"}, {"Emerging Markets", "Impact Investing"}, {"Artificial Intelligence", "Robotics"}, {"Human Rights", "Social Advocacy"}, {"Cryptocurrency", "Decentralized Finance"}, {"Health and Wellness", "Nutrition"}, {"Public Speaking", "Leadership Development"}, {"Policy Analysis", "Political Campaigning"}, {"Sustainable Development", "Environmental Policy"}, {"Blockchain Technology", "Data Privacy"}, {"Fine Arts", "Photography"}, {"Music Production", "Audio Engineering"}, {"Graphic Design", "Illustration"}, {"Athletics", "Sports Analytics"}, {"Fashion Design", "Trend Analysis"}, {"Adventure Sports", "Outdoorsmanship"}, {"Personal Fitness", "Nutrition"}, {"Writing", "Creative Fiction"}, {"Photography", "Visual Storytelling"}, {"Art Direction", "Multimedia Design"}, {"Gaming", "Game Design"}, {"Public Relations", "Media Strategy"}, {"Poetry", "Spoken Word"}, {"Film Making", "Screenwriting"}, {"Dance Performance", "Choreography"}, {"Mindfulness", "Meditation"}, {"Community Service", "Volunteerism"}, {"Debate", "Oratory Skills"}, {"International Trade", "Foreign Affairs"}, {"Youth Mentorship", "Teaching"}, {"Fundraising", "Non-Profit Management"}, {"Public Policy", "Government Affairs"}, {"Software Engineering", "App Development"}, {"Entrepreneurship", "Startup Development"}, {"Retail Management", "Customer Experience"}, {"Computer Science", "Algorithm Design"}, {"Machine Learning", "Big Data"}, {"Web Development", "UI/UX Design"}, {"Event Management", "Public Relations"}, {"Strategic Planning", "Consulting"}, {"Public Health", "Medical Research"}]



oopulation_data = {
    "0_degree": zero_degree,
    "1_degree": one_degree,
    "activities": activities,
    "interests": interests
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

