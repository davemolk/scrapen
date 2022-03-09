# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose

def clean(value):
    if '\xa0' in value:
        value = value.replace('\xa0', ' ')
    return value

class SkItem(scrapy.Item):
    name = scrapy.Field(
        input_processor=MapCompose(clean),
    )
    link = scrapy.Field()