
def compare_prices(filtered_df):
    currency_symbol = filtered_df['price'].str.extract('([^\d., ]+)', expand=False).iloc[0]

    # Remove the currency symbol and convert price to numeric
    filtered_df['price'] = filtered_df['price'].replace('[^0-9.]', '', regex=True).astype(float)

    # Get the item(s) with the lowest price
    lowest_price = filtered_df['price'].min()
    items_with_lowest_price = filtered_df[filtered_df['price'] == lowest_price][['name', 'price','site']]

    # Attach the currency symbol back to the result
    items_with_lowest_price['price'] = currency_symbol + items_with_lowest_price['price'].astype(str)

    return items_with_lowest_price