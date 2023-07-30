# DataWeaver

## Overview

DataWeaver is a powerful web scraping and data processing Python project designed to gather product information from various e-commerce websites, perform data cleaning and transformation, and compare prices to find the best deals. It leverages the Scrapy framework for web scraping and utilizes pandas for efficient data manipulation.

## Features

- **Web Scraping:** DataWeaver scrapes product information from different e-commerce websites to compile a dataset for analysis.

- **Data Cleaning:** The collected data undergoes a cleaning process to handle inconsistencies and ensure uniformity.

- **Data Transformation:** Advanced filtering mechanisms are applied to transform the data, ensuring only relevant information is considered for price comparison.

- **Price Comparison:** DataWeaver compares product prices across multiple e-commerce platforms, providing insights into the best deals available.

- **Proxy Rotation:** The project incorporates proxy rotation for enhanced scraping capabilities, ensuring uninterrupted data collection.

- **Negation Feature:** Users can provide a list of words to negate, allowing for more accurate and refined results by excluding specified keywords from product titles.

## Usage

- Clone this repository
- create a virtual environment [python3 -m venv "name of your virtual environment"] e.g `python3 -m venv venvDataWeaver`
- Run `pip install -r requirements.txt`
- Run the `main.py` file and  it will ask for keyword and words to negate. Enter the negated words seperate them with commas
- It displays the best price on the terminal

## Contributing

Contributions are welcome! Feel free to raise issues or submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE)





