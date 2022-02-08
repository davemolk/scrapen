import scrapy


class SandySpider(scrapy.Spider):
    name = 'sandy'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        links = response.css("ul.nav-list li ul li a::attr(href)")
        for link in links:
            yield response.follow(link, callback=self.parse_books)

    def parse_books(self, response):
        books = response.css('ol.row li')
        for book in books:
            yield {
                'name': book.css('article.product_pod h3 a::attr(title)').get(),
                'price': book.css('div.product_price p::text').get(),
            } 

        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse_books)