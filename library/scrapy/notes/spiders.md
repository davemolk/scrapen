# scrapy.Spider
name
allowed_domains
start_urls
custom_settings

you can use start_requests instead of start_urls:

def start_requests(self):
    yield scrapy.Request("http://example.com/1", self.parse_first)
    yield scrapy.Request("http://example.com/2", self.parse_second)
    yield scrapy.Request("http://example.com/3", self.parse_third)


# CrawlSpider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

need to set rules and can't name your parse function 'parse'

rules are always a tuple and you don't need to specify a callback function for the first rule...scrapy will automatically follow those urls

rule parameters: link_extractor, callback, cb_kwargs, follow, process_links, process_request, errback

