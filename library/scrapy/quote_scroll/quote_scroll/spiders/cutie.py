import scrapy
import json


class CutieSpider(scrapy.Spider):
    name = 'cutie'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/api/quotes?page=1']

    def parse(self, response):
        data = json.loads(response.text)
        for quote in data["quotes"]:
            yield {
                "author": quote["author"]["name"],
                "quote": quote['text'],
                "tags": quote['tags'],
            }
        if data['has_next']:
            next_page = data['page'] + 1
            url = f'https://quotes.toscrape.com/api/quotes?page={next_page}'
            yield scrapy.Request(url=url, callback=self.parse)