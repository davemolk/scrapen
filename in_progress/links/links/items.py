# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags

class LinksItem(scrapy.Item):
    page_title = scrapy.Field(
        input_processor = MapCompose(remove_tags),
        output_processor = TakeFirst(),
    )
    link = scrapy.Field(
        input_processor = MapCompose(remove_tags),
        output_processor = TakeFirst(),
    )
