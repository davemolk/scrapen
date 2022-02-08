# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from urllib.parse import urljoin

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags

def strip(value):
    if value is not None:
        return value.strip()
    return value

def make_link(value):
    base_url = 'https://github.com/'
    return urljoin(base_url, value)

class GithubTrendingItem(scrapy.Item):
    name = scrapy.Field(
        # input_processor = MapCompose(strip), 
        # output_processor = TakeFirst()
    )
    link = scrapy.Field(
        input_processor = MapCompose(make_link),
        output_processor = TakeFirst(),
    )
    desc = scrapy.Field(
        input_processor = MapCompose(strip),
        output_processor = TakeFirst(),
    )
    language = scrapy.Field(
        output_processor = TakeFirst(),
    )
    total_stars = scrapy.Field()
    stars_today = scrapy.Field()
    date = scrapy.Field()