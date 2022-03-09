import scrapy
from book_links.items import BookLinksItem

class V2(scrapy.Spider):
    name  = 'v2'
    start_urls = ['http://books.toscrape.com']
    allowed_urls = ['books.toscrape.com']

    def parse(self, response):
        item = BookLinksItem()
        for book in response.css('ol.row li'):
            item['title'] = book.css('article.product_pod h3 a::text').get()
            item['price'] = book.css('article.product_pod p.price_color::text').get().replace('£', '')
            deet_link = book.css('article.product_pod h3 a::attr(href)').get()
            deet_link = response.urljoin(deet_link)

            yield scrapy.Request(deet_link, 
                                self.parse_details, 
                                cb_kwargs={'item': item})
        
        next_page = response.css('ul.pager li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)


    def parse_details(self, response, item):
        item['link'] = response.url
        item['description'] = response.css('div#product_description + p::text').get()

        return item