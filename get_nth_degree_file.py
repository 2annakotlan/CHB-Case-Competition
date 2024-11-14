from population_data_file import population_df
df_degree = population_df.copy()

def get_nth_degree(df_degree, n):
    df_degree[f'{n}_degree'] = None  # new column for nth degree connections
    for index, row in df_degree.iterrows():  # for every person in the dataframe...
        previous_degree = row[f'{n-1}_degree']  # get list of their previous degree connections
        all_previous_degrees = set()  # get list of ALL previous degree connections
        for i in range(0, n): all_previous_degrees.update(row[f'{i}_degree'])
        n_degree_set = set()  # initialize set to store unique nth degree values
        for i in previous_degree:  # for each person in the previous-degree connections list...
            matching_row = df_degree[df_degree['0_degree'] == i]  # find the row where the 'name' matches the current previous-degree connection
            if not matching_row.empty:  # as long as that person exists in the list...
                n_degree_set.update(set(matching_row[f'{n-1}_degree'].values[0]) - all_previous_degrees) # extract their nth degree connections (excluding all_previous_degree values) and append it to the set
        df_degree.at[index, f'{n}_degree'] = n_degree_set  # save to dataframe as a set of unique connections

    # Remove nth-degree connections that don't exist in the dataset
    for index, row in df_degree.iterrows(): # for every person in the dataframe...
        nth_degree_names = row[f'{n}_degree'] # store their nth degree connection names
        valid_names = nth_degree_names & set(df_degree['0_degree'])  # names appear in both the nth degree connection names and the records
        df_degree.at[index, f'{n}_degree'] = valid_names  # update nth-degree column with valid names

