import scrapy

class WalmartSpider(scrapy.Spider):
    site = 'wallmart'
    keyword = 'yamaha ck88'
    name = f'{site}_spider'

    def start_requests(self):
        url = f'https://www.walmart.com/search/?query={self.keyword}'

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

        yield scrapy.Request(url=url, headers=headers, callback=self.parse)

    def parse(self, response):
        import re

        # Find all the product items on the page
        # product_items = response.xpath('//div[@id="searchProductResult"]/div')
        product_items = response.xpath('//div[@id="results-container"]/following-sibling::section[1]//div')

        products = []
        for item in product_items:
            name = item.xpath('.//span/span[@data-automation-id="product-title"]/text()').get()
            if name:
                name = name.strip()

            price = item.xpath('.//div[@data-automation-id="product-price"]/span/text()').get()
            if price:
                price = re.sub(r"[a-zA-Z]", "", price).strip()

            product = {
                'name': name,
                'price': price,
                'site': self.site

            }
            if product not in products:
                products.append(product)
                yield product 
                
            # print(products)