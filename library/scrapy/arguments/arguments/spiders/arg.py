import scrapy


class ArgSpider(scrapy.Spider):
    name = 'arg'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/login']


    def start_requests(self):
        print()
        yield scrapy.Request(f'https://quotes.toscrape.com/tag/{self.tag}')
    
    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)
        for q in response.css('div.quote'):
            yield {
                "text": q.css('span.text::text').get(),
            }