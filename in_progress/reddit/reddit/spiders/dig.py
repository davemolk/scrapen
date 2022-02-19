import scrapy


class DigSpider(scrapy.Spider):
    name = 'dig'
    allowed_domains = ['old.reddit.com']
    start_urls = ['http://old.reddit.com/']

    def parse(self, response):
        pass
