import scrapy
from scrapy.loader import ItemLoader
from sk.items import SkItem

class SmittenKitchen(scrapy.Spider):
    name = 'sk'
    allowed_domains = ['smittenkitchen.com']
    start_urls = [
        "https://smittenkitchen.com/recipes/fruit/?format=list",
        # 'https://smittenkitchen.com/recipes/meat/?format=list',
        # 'https://smittenkitchen.com/recipes/sweets/?format=list',
        # 'https://smittenkitchen.com/recipes/vegetable/?format=list',
        ]

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Safari/537.36',
        }


    def parse(self, response):
        self.logger.info('visiting %s', response.url)        

        for dish in response.css('main#main li'):
            loader = ItemLoader(item=SkItem(), selector=dish)
            loader.add_css('name', 'a::text')
            loader.add_css('link', 'a::attr(href)')
            deet_link = response.urljoin(dish.css('a::attr(href)').get())


            yield scrapy.Request(deet_link,
                                self.parse_details,
                                cb_kwargs={'loader': loader})

            # yield l.load_item()
        
    def parse_details(self, response, loader):
        title = response.css('title::text').get()
        loader.add_value('title', title)

        yield loader.load_item()