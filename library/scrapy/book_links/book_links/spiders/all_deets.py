import scrapy

# normally what a crawl spider would do...
class DeetsSpider(scrapy.Spider):
    name = 'deets'
    start_urls = ['https://books.toscrape.com']
    allowed_urls = ['books.toscrape.com']

    # get category links from sidebar
    def parse(self, response):
        for link in response.css('ul.nav-list li ul li a::attr(href)'):
            yield response.follow(link.get(), callback=self.get_links)

    # get detail links per item, check and follow if multiple pages per category
    def get_links(self, response):
        for link in response.css('h3 a::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_details)
        
        next_page = response.css('li.next a::attr(href)').get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.get_links)

    def parse_details(self, response):
        header = []
        data = []
        for row in response.css('table tr'):
            header.append(row.css('th::text').get())
            data.append(row.css('td::text').get())
        yield{
            'title': response.css('h1::text').get(),
            'price': response.css('p.price_color').get(),
            'availability': response.css('p.instock::text').getall()[1].strip(),
            'description': response.css('div#product_description + p::text').get(),
            'table': dict(zip(header, data))
        }