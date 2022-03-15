# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags

def loader(response):
        item = ErrorLinkItem()
        item['url'] = response.url
        item['status'] = response.status
        item['referer'] = response.request.headers.get('Referer', 'header unavailable')
        return item


class LinksItem(scrapy.Item):
    page_title = scrapy.Field(
        input_processor = MapCompose(remove_tags),
        output_processor = TakeFirst(),
    )
    link = scrapy.Field(
        input_processor = MapCompose(remove_tags),
        output_processor = TakeFirst(),
    )

class ErrorLinkItem(scrapy.Item):
    url = scrapy.Field()
    referer = scrapy.Field()
    status = scrapy.Field()