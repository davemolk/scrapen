import scrapy


class PagesSpider(scrapy.Spider):
    name = 'pages'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        for book in response.css('ol.row li'):
            yield {
                'name': book.css('article.product_pod h3 a::text').get(),
                'price': book.css('article.product_pod p.price_color::text').get(),
                'link': book.css('article.product_pod h3 a::attr(href)').get(),
            }

        next_page = response.css('ul.pager li.next a::attr(href)').get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)