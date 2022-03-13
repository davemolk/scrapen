import scrapy
import playwright

class ArgSpider(scrapy.Spider):
    name = "arg"
    # url = 'https://www.davemolk.com']

    def __init__(self, url=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.allowed_domains = [f'{url}']
        self.start_urls = [f'https://{url}']

    def parse(self, response):
        for link in response.css('a::attr(href)'):
            yield response.follow(
                link, 
                callback=self.parse_details,
                meta={"playwright": True, "playwright_include_page": True,},
            )

    # def start_requests(self):
    #     yield scrapy.Request(
    #         url = f'https://www.{self.url}',
    #         meta={"playwright": True, "playwright_include_page": True,},
    #         errback = self.errback,
    #     )
        
    async def parse_details(self, response):
        page = response.meta["playwright_page"]
        title = await page.title()
        for link in response.css('a::attr(href)'):
            yield response.follow(
                link, 
                callback=self.parse_details,
                meta={"playwright": True, "playwright_include_page": True,},
            )
            # print("****************************************************************", link)
            # self.parse(link)
        await page.close()
        yield {'title': title}

        # for link in response.css('a::attr(href)'):
        #     link = response.urljoin(link.get())
        #     yield scrapy.Request(link, callback=self.parse_details)
    
    # async def parse_details(self, response):
    #     page = response.meta["playwright_page"]
    #     title = await page.title()
    #     await page.close()
    #     yield {'title': title}

    async def errback(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()