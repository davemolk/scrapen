from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from links.items import LinksItem

from links.constants import IGNORED_EXTENSIONS

class Link(CrawlSpider):
    name = 'l'

    # bring in rotating UA soon
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Safari/537.36',
    }
    
    rules = (
        Rule(LinkExtractor(
            allow=(),
            deny_extensions=IGNORED_EXTENSIONS
            ), 
            callback="parse_item", 
            follow=True),
    )

    
    def __init__(self, url=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.allowed_domains = [f'{url}']
        self.start_urls = [f'https://{url}']

    def parse_item(self, response):
        item = LinksItem()
        item['page_title'] = response.css('title::text').get()
        item['link'] = response.url
        
        yield item