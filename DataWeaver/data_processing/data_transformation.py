
def filter_data(dataframe, keyword, negated_keywords):

    dataframe["name"].fillna("", inplace=True)

    # Convert descriptions to lowercase for case-insensitive comparison
    dataframe["name"] = dataframe["name"].str.lower()

    # Handle single-word keywords directly
    if len(keyword.split()) == 1:
        filtered_df = dataframe[dataframe["name"].str.contains(keyword, case=False)]
    else:
        # Handle multi-word keywords sequentially
        filtered_df = dataframe.copy() 
        words = keyword.split()
        for word in words:
            filtered_df = filtered_df[filtered_df["name"].str.contains(word, case=False)]

    # Apply negation filtering
    for negated_keyword in negated_keywords:
        filtered_df = filtered_df[~filtered_df["name"].str.contains(negated_keyword, case=False)]

    return filtered_df
