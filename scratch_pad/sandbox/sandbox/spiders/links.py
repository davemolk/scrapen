import scrapy
from scrapy.spidermiddlewares.httperror import HttpError
from scrapy.spiders import SitemapSpider, CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from sandbox.items import LinksItem, loader

from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError


class Link(CrawlSpider):
    name = 'l'

    # bring in rotating UA soon
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    }
    
    rules = (
        Rule(LinkExtractor(
            allow=(),
            ), 
            callback="parse_item", 
            errback="parse_error",
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

    def parse_error(self, failure):
        # log all failures
        self.logger.error(repr(failure))

        if failure.check(HttpError):
            response = failure.value.response
            yield loader(response)

        elif failure.check(DNSLookupError):
            # this is the original request
            request = failure.request
            self.logger.error(f'DNSLookupError on {request.url}')

        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.logger.error(f'TimeoutError on {request.url}')
