import scrapy


# ignore robots
class DigSpider(scrapy.Spider):
    name = 'dig'
    allowed_domains = ['old.reddit.com']
    start_urls = ['http://old.reddit.com/']

    def parse(self, response):
        for post in response.css('div#siteTable div.thing'):
            yield {
                'blurb': post.css('a::text').get(),
                'sub': post.css('a.subreddit::text').get(),
            }
