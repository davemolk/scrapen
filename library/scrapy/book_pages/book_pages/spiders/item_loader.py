import scrapy
from scrapy.loader import ItemLoader

from book_pages.items import BookPagesItem


class ItemLoaderSpider(scrapy.Spider):
    name = 'item_loader'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/catalogue/page-1.html']

    def parse(self, response):
        for book in response.css('ol.row li'):
            loader = ItemLoader(item = BookPagesItem(), selector=book)
            loader.add_css('name', 'article.product_pod h3 a')
            loader.add_css('price', 'article.product_pod p.price_color')
            loader.add_css('link', 'article.product_pod h3 a::attr(href)')
           
            yield loader.load_item()

        next_page = response.css('ul.pager li.next a::attr(href)').get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)