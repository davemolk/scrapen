import scrapy
from scrapy.loader import ItemLoader
from sk.items import SkItem

class SmittenKitchen(scrapy.Spider):
    name = 'sk'
    allowed_domains = ['smittenkitchen.com']
    start_urls = [
        "https://smittenkitchen.com/recipes/fruit/?format=list",
        'https://smittenkitchen.com/recipes/meat/?format=list',
        'https://smittenkitchen.com/recipes/sweets/?format=list',
        'https://smittenkitchen.com/recipes/vegetable/?format=list',
        ]

    def parse(self, response):
        self.logger.info('visiting %s', response.url)        

        for dish in response.css('main#main li'):
            l = ItemLoader(item=SkItem(), selector=dish)
            l.add_css('name', 'a::text')
            l.add_css('link', 'a::attr(href)')

            yield l.load_item()