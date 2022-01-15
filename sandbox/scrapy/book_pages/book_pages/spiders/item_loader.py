import scrapy

from book_pages.items import BookPagesItem


class ItemLoaderSpider(scrapy.Spider):
    name = 'item_loader'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/catalogue/page-1.html']

    def parse(self, response):
        item = BookPagesItem()
        for book in response.css('ol.row li'):
            item['name'] = book.css('article.product_pod h3 a::text').get()
            item['price'] = book.css('article.product_pod p.price_color::text').get().replace('£', '')
            item['link'] = book.css('article.product_pod h3 a::attr(href)').get()
    
            yield item

        next_page = response.css('ul.pager li.next a::attr(href)').get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)