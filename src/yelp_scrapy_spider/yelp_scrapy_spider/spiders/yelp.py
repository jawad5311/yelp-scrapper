import scrapy


class YelpSpider(scrapy.Spider):
    name = "yelp"
    allowed_domains = ["yelp.com"]
    start_urls = ["http://www.yelp.com/search?find_desc=gym&find_loc=San+Francisco"]

    def parse(self, response):
        urls = response.css('h3.css-1agk4wl span a.css-1m051bw::attr(href)').getall()

        for url in urls:
            url = f'http://www.yelp.com{url}'
            yield scrapy.Request(
                url=url,
                callback=self.parse_item
            )

    def parse_item(self, response):
        name = response.css("h1.css-1se8maq::text").get()
        phone_no = response.css(".border-color--default__09f24__NPAKY+ .border--top__09f24__exYYb .vertical-align-middle__09f24__zU9sE .css-1p9ibgf::text").get()
        website = response.css(".css-1p9ibgf .css-1um3nx::text").get()

        # Business Address
        addr_1 = response.css(".css-1um3nx .raw__09f24__T4Ezm::text").get()
        addr_2 = response.css(".css-1sb02f4 .raw__09f24__T4Ezm::text").get()
        addr_3 = response.css("address+ .css-gutk1c::text").get()
        addr_4 = response.css(".css-gutk1c+ .css-gutk1c::text").get()

        address = f'{addr_1},{addr_2},{addr_3},{addr_4}'

        print(name)
        print(phone_no)
        print(website)

        print(address)

        yield {
            'name': name,
            'phone': phone_no,
            'website': website,
            'address': address
        }

