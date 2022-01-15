import scrapy
from scrapy.crawler import CrawlerProcess

url = 'https://www.oldtowntequila.com/mezcal/?sort=newest&page=1'

class MezcalSpider(scrapy.Spider):
    name = 'agave'

    def start_requests(self):
        yield scrapy.Request(url)

    def parse(self, response):
        products = response.css('li.product')

        for item in products:
            yield {
                'name': item.css('p.card-text--brand::text').get(),
                'price': item.css('span.price--main::text').get(),
            }   
        next_page = response.css('li.pagination-item--next a.pagination-link::attr(href)').get()
        while next_page is not None:
            yield response.follow(next_page, callback=self.parse)

process = CrawlerProcess(settings = {
    'FEED_URI': 'mezcal.csv',
    'FEED_FORMAT': 'csv',
})

process.crawl(MezcalSpider)
process.start()