import scrapy


class YelpSpider(scrapy.Spider):
    name = "yelp"
    allowed_domains = ["yelp.com"]
    start_urls = ["http://yelp.com/"]

    def parse(self, response):
        pass
