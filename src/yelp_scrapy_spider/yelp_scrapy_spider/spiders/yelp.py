import scrapy


class YelpSpider(scrapy.Spider):
    name = "yelp"
    allowed_domains = ["yelp.com"]
    start_urls = ["http://www.yelp.com/search?find_desc=gym&find_loc=San+Francisco"]

    def parse(self, response):
        titles = response.css('.css-1egxyvc .css-1m051bw::text').getall()
        print("THESE ARE TITLES")
        print(titles)
        print(len(titles))
        for title in titles:
            # yield {
            #     'title': title,
            # }
            print(title)
