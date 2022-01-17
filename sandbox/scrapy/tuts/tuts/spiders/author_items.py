import scrapy
from scrapy.loader import ItemLoader 

from tuts.items import TutsItem


class AuthorItemsSpider(scrapy.Spider):
    name = 'author_items'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        author_page_links = response.css('.author + a')
        yield from response.follow_all(author_page_links, self.parse_author)

        pagination_links = response.css('li.next a')
        yield from response.follow_all(pagination_links, self.parse)

    def parse_author(self, response):
        # def extract_with_css(query):
        #     return response.css(query).get(default='').strip()
        
        # yield {
        #     'name': extract_with_css('h3.author-title::text'),
        #     'birthdate': extract_with_css('.author-born-date::text'),
        #     'bio': extract_with_css('.author-description::text'),
        # }

        
        il = ItemLoader(item=TutsItem(), response=response)
        il.add_css('name', 'h3.author-title')
        il.add_css('birthdate', '.author-born-date')
        il.add_css('bio', '.author-description')

        yield il.load_item()