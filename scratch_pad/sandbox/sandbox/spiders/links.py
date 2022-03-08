from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class Link(CrawlSpider):
    name = 'l'
    allowed_domains = ['molkmusic.com']
    start_urls = ['https://www.molkmusic.com']

    rules = Rule(LinkExtractor(allow=(r'/blog')), 
                callback="parse_item", 
                follow=True),

    def parse_item(self, response):
        # self.logger.info('landed on %s', response.url)
        print()
        yield {
            "title": response.css('title::text').get(),
            'url': response.url
        }