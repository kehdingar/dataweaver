from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher
from comparison.price_comparison import compare_prices
from data_processing.data_cleaning import clean_data
from data_processing.data_transformation import filter_data

from web_scraping.ebay_scrapy import EbaySpider 
from web_scraping.amazon_scrapy import AmazonSpider
from web_scraping.walmart_scrapy import WalmartSpider
import pandas as pd
import json

# Initialize an empty list to store results
result_list = []

def collect_results(item, response, spider):
    global result_list
    result_list.append(item)  # Append the individual item to the list

dispatcher.connect(collect_results, signal=signals.item_scraped)

def run_scrapers(keyword,negated_keywords):
    process = CrawlerProcess()

    process.crawl(EbaySpider, keyword=keyword)
    process.crawl(AmazonSpider, keyword=keyword)
    process.crawl(WalmartSpider, keyword=keyword)

    process.start()

    # Create a DataFrame after all items are collected
    combined_df = pd.DataFrame(result_list)

    # Perform data cleaning and filtering (optional)
    cleaned_df = clean_data(combined_df)
    filtered_df = filter_data(cleaned_df,keyword,negated_keywords)
    best_price_df = compare_prices(filtered_df)

    # Convert product list to JSON for frontend
    data_best_price = best_price_df.to_dict("records")
    iltered_price_list = filtered_df.to_dict("records")

    spider_classes = [EbaySpider, AmazonSpider,WalmartSpider]  

    # Print the site names of the spiders
    site_names = [spider_class.site for spider_class in spider_classes]
    print("\n\nSite names:", json.dumps(site_names, indent=4))    

    # You can now use `json_data` in your React application
    print(f"\n\nJSON data for frontend best price:\n",json.dumps(data_best_price, indent=4))
    print(f"\n\nJSON data for frontend filtered price:\n", json.dumps(iltered_price_list, indent=4),"\n\n")

if __name__ == "__main__":
    keyword = input("Enter the search keyword: ")
    negated_keywords = input("Enter negated keywords (comma-separated): ").split(",")
    run_scrapers(keyword, negated_keywords)