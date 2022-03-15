import scrapy
from scrapy.spidermiddlewares.httperror import HttpError
from scrapy.spiders import SitemapSpider, CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from links.items import LinksItem, loader

from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError

from links.constants import IGNORED_EXTENSIONS


class ProblematicLinks(scrapy.Spider):
    name = '404'
    handle_httpstatus_list = [200, 403, 404, 500]

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Safari/537.36',
    }
    
    def __init__(self, url=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.allowed_domains = [f'{url}']
        self.start_urls = [f'https://{url}']

    def parse(self, response):
        if response.status == 404:
            yield loader(response)

        elif response.status == 403:
            yield loader(response)

        elif response.status == 500:
            yield loader(response)

        else:
            self.logger.info("No problematic links")


class MapSpider(SitemapSpider):
    name = 'map'

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Safari/537.36',
    }
    
    def __init__(self, url=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.allowed_domains = [f'{url}']
        self.sitemap_urls = [f'https://{url}/sitemap.xml']

    def parse(self, response):
        yield {
            'title': response.css('title::text').get(),
            'url': response.url,
        }


class MapSpider(SitemapSpider):
    name = 'mappy'

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Safari/537.36',
    }
    
    def __init__(self, url=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.allowed_domains = [f'{url}']
        self.sitemap_urls = [f'https://{url}/sitemap.xml']

    def parse(self, response):
        yield {
            'title': response.css('title::text').get(),
            'url': response.url,
        }


class Link(CrawlSpider):
    name = 'l'

    # bring in rotating UA soon
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Safari/537.36',
    }
    
    # not kicking in when I have the start_requests
    rules = (
        Rule(LinkExtractor(
            allow=(),
            deny_extensions=IGNORED_EXTENSIONS
            ), 
            callback="parse_item", 
            errback="parse_error",
            follow=True),
    )
    
    def __init__(self, url=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.allowed_domains = [f'{url}']
        self.start_urls = [f'https://{url}']

    def start_requests(self):

        sitemap = 'https://' + self.allowed_domains[0].split('/')[0] + '/sitemap.xml'
        
        yield scrapy.Request(
            url=sitemap, 
            callback=self.parse_map,
            errback=self.parse_error,    
        )

        print("************************ second yield")
        yield scrapy.Request(
            url=self.start_urls[0], 
            callback=self.parse_item,
            errback=self.parse_error,
        )

    def parse_map(self, response):
        pass
        # print("************************", response.status)
        # for a in response.css('a::attr(href)'):
        #     yield {
        #         'title': response.css('title::text').get(),
        #         'url': response.url,
        #     }


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
