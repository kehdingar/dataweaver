import scrapy

class EbaySpider(scrapy.Spider):
    site = 'ebay'
    keyword = ''
    name = f'{site}_spider'


    def start_requests(self):
        url = f'https://www.ebay.com/sch/i.html?_nkw={self.keyword}'

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

        yield scrapy.Request(url=url, headers=headers, callback=self.parse)

    def parse(self, response):
        # Find all the product items on the page
        product_items = response.css('li.s-item .s-item__title')

        # Extract relevant information from each product item
        products = []
        for item in product_items:
            name = item.css('::text').get()
            if name:
                name = name.strip()

            price = item.xpath(
                '../../div[@class="s-item__details clearfix"]/div[@class="s-item__detail s-item__detail--primary"]/span[@class="s-item__price"]/text()'
            ).get()
            if price:
                price = price.strip()

            rating = item.css('span.s-item__reviews-count::text').get()
            if rating:
                rating = rating.strip()

            product = {
                'name': name,
                'price': price,
                'rating': rating,
                'site': self.site

            }
            products.append(product)
            yield product 
        
        # print(products)
    