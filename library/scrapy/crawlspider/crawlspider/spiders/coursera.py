from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class Course(CrawlSpider):
    name = 'learn'
    allowed_domains = ['coursera.org']
    start_urls = ['https://www.coursera.org']

    rules = (
        Rule(LinkExtractor(allow=(r'/learn/\w*')), callback='parse_item'),
        Rule(LinkExtractor(deny=(r'/browse/\w*'))),
        Rule(LinkExtractor(deny=(r'/login/\w*'))),
        Rule(LinkExtractor(deny=(r'/signup/\w*'))),
    )

    def parse_item(self, response):
        self.logger.info('A response from %s just arrived!', response.url)
        yield {
            "title": response.css('title::text').get(),
        }

# thinking about porting this over into scrapy...
# http://go-colly.org/docs/examples/coursera_courses/