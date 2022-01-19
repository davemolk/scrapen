import scrapy


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        for link in response.css('ul.nav-list li ul li a::attr(href)'):
            yield(response.follow(link.get(), callback=self.parse_categories))
    
    def parse_categories(self, response):
        books = response.css('ol.row li')
        for book in books:
            yield {
                'name': book.css('article.product_pod h3 a::text').get(),
                'price': book.css('div.product_price p::text').get(),
            }            
