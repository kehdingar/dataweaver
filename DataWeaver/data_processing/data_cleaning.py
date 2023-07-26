def clean_data(dataframe):
    # Drop duplicate rows
    dataframe.drop_duplicates(inplace=True)

    dataframe.dropna(how='all', inplace=True)

    # Reset the index after dropping rows
    dataframe.reset_index(drop=True, inplace=True)

    return dataframe
