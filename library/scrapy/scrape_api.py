import json

import scrapy


class QuoteSpider(scrapy.Spider):
    name = 'quote'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/api/quotes?page=1']
    page = 1
    
    def parse(self, response):
        # convert string to dictionary
        data = json.loads(response.text)
        for quote in data['quotes']:
            yield {
                'quote': quote['text'].strip()
            }
        if data['has_next']:
            self.page += 1
            url = f'https://quotes.toscrape.com/api/quotes?page={self.page}'
            yield scrapy.Request(url=url, callback=self.parse)

