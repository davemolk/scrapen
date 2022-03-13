import scrapy
from scrapy_playwright.page import PageCoroutine

class PWSpider(scrapy.Spider):
    name = 'pw'

    url = 'https://shoppable-campaign-demo.netlify.app/#/'

    def start_requests(self):
        yield scrapy.Request(self.url, meta = dict(
                playwright = True,
                playwright_include_page = True,
                playwright_page_coroutines = [
                    PageCoroutine('wait_for_selector', 'div#productListing')
                ]
            )
        )

    async def parse(self, response):
        for product in response.css('div.card-body'):
            yield {
                'title': product.css('h3::text').get(),
                'price': product.css('div.form-group label::text').get(),
            }