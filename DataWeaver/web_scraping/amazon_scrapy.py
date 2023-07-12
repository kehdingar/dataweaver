import scrapy

class AmazonSpider(scrapy.Spider):
    site = 'amazon'
    keyword = ''
    name = f'{site}_spider'

    def start_requests(self):
        url = f'https://www.amazon.com/s?k={self.keyword}'

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

        yield scrapy.Request(url=url, headers=headers, callback=self.parse)

  
    def parse(self, response):

        product_items = response.xpath('//div[@data-asin]')
        products = []
        for item in product_items:
            name = item.xpath('.//h2//text()').getall()
            name = ' '.join(name).strip()
            if name:
                name = name.strip()

            # Check if "No featured offers available" is present
            no_offers_text = item.xpath('.//span[contains(text(), "No featured offers available")]')
            if no_offers_text:
                # Extract price from the subsequent span with class "a-color-base"
                price = item.xpath('.//span[@class="a-color-base"]/text()').get()
                if price:
                    price = price.strip()
            else:
                # Extract price directly
                price = item.css('span.a-price span.a-offscreen::text').get()
                if price:
                    price = price.strip()

            rating = item.css('span.a-icon-alt::text').get()
            if rating:
                rating = rating.strip()

            product = {
                'name': name,
                'price': price,
                'rating': rating,
                'site': self.site
            }
    
            products.append(product)
            # yield product to be used in main
            yield product 

            # print(products)