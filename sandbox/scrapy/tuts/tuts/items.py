# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags

def strip(text: str):  
    return text.strip().replace('\n', ' ')


class TutsItem(scrapy.Item):
    name = scrapy.Field(input_processor = MapCompose(remove_tags, strip), 
                        output_processor = TakeFirst())
    birthdate = scrapy.Field(input_processor = MapCompose(remove_tags), 
                        output_processor = TakeFirst())
    bio = scrapy.Field(input_processor = MapCompose(remove_tags, strip), 
                        output_processor = TakeFirst())