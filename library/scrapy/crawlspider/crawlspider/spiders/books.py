from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class GetLinks(CrawlSpider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/catalogue/category/books/sequential-art_5/page-1.html']

    le_book_details = LinkExtractor(restrict_css='h3 > a') # only going for a kiddos of h3
    le_next = LinkExtractor(restrict_css='.next > a') # next button
    le_categories = LinkExtractor(restrict_css='ul.nav-list li ul li a')
    
    rule_book_details = Rule(
        le_book_details, 
        callback='parse_item', 
        follow=False,
    )
    rule_next_book = Rule(
        le_next,
        follow=True,
    )
    rule_categories = Rule(
        le_categories,
        callback='parse_item',
        follow=True,
    )

    rules = (
        rule_book_details,
        rule_next_book,
        rule_categories,
    )

    def parse_item(self, response):
        yield {
            'title': response.css('h1::text').get(), 
            'price': response.css('p.price_color::text').get(),
            'available': response.css('p.instock::text').getall()[1].strip(),
            # 'description': response.css('div#product_description + p::text').get(),
        }