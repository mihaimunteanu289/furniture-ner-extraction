import pandas as pd
from typing import Generator
from scrapy.http import Response, Request
from scrapy import Spider, Request, Item, Field
from scrapy.linkextractors import LinkExtractor
from twisted.internet.error import TimeoutError, TCPTimedOutError

# The path to the CSV file which contains the product URLs
CSV_PATH = "../../../../data/furniture stores pages.csv"

# Defining a new item type 'Product' with fields 'product_name', 'url', and 'error'
class Product(Item):
    product_name = Field()
    url = Field()
    error = Field()

# Defining a new spider 'ProductSpider'
class ProductSpider(Spider):
    name = 'ProductSpider'
    link_extractor = LinkExtractor(allow=r'/products/(.+)') # Regex for extracting product URLs

    # Setting the output format, encoding, and overwrite option for the Scrapy feed
    custom_settings = {
        'FEEDS': {
            'products/products_file.json': {
                'format': 'json',
                'encoding': 'utf8',
                'overwrite': True
            }
        },
        'ROBOTSTXT_OBEY': False
    }


    # This function reads the CSV file and starts the request process
    def start_requests(self) -> Generator[Request, None, None]:
        try:
            ds = pd.read_csv(CSV_PATH) # Reading the CSV file
            products = ds.iloc[:, 0].tolist() # Get the first two product URLs from the CSV
        except Exception as e:
            # Log error message if there's a problem reading the CSV
            self.logger.error(f"Error reading CSV: {str(e)}")
            return

        # Make requests for each product URL and call 'parse_product_list' function when a response is received
        for product_url in products:
            yield Request(url=product_url, callback=self.parse_product_list, errback=self.handle_error)

    # This function extracts product URLs from the received response and initiates requests to them
    def parse_product_list(self, response: Response) -> Generator[Request, None, None]:
        product_links = self.link_extractor.extract_links(response) # Extract all product links

        # Make requests for each extracted product link and call 'parse_product' function when a response is received
        for link in product_links:
            # Skip URLs that end with "/"
            if not link.url.endswith('/'):
                yield Request(url=link.url, callback=self.parse_product, errback=self.handle_error)

    # This function extracts the product name from the received response
    def parse_product(self, response: Response) -> Generator[Product, None, None]:
        product_name = response.css('h1::text').get()
        # product_name = response.xpath("//meta[@property='og:title']/@content").get()
        if product_name:
            # If a product name is found, yield a new Product item with the name and URL
            yield Product(product_name=product_name.strip(), url=response.url)
        else:
            # If no product name is found, yield a new Product item with the URL and error message
            yield Product(url=response.url, error="No product name found")
            
    # This function handles any errors that occur during the request process
    def handle_error(self, failure) -> Generator[Product, None, None]:
        # If an error occurs, yield a new Product item with the URL and error message
        yield Product(url=failure.request.url, error=str(failure.value))
