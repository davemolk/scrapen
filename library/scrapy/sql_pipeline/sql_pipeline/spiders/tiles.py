import scrapy
from scrapy.loader import ItemLoader

from sql_pipeline.items import SqlPipelineItem


class TilesSpider(scrapy.Spider):
    name = 'tiles'
    allowed_domains = ['magnatiles.com']
    start_urls = ['http://magnatiles.com/products/page/1/']

    def parse(self, response):
        for product in response.css('li.product'):
            il = ItemLoader(item=SqlPipelineItem(), selector=product)
            il.add_css('sku', 'a.button::attr(data-product_sku)')
            il.add_css('name', 'h2.woocommerce-loop-product__title')
            il.add_css('price', 'span.woocommerce-Price-amount bdi')
            
            yield il.load_item()

        next_page = response.css('ul.page-numbers a.next::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)