# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from urllib.parse import urljoin
import re
import scrapy
from itemloaders.processors import TakeFirst, MapCompose

def strip(value):
    if value is not None:
        return value.strip()
    return value

def make_link(value):
    base_url = 'https://github.com/'
    return urljoin(base_url, value)

def get_stars(value):
    clean = re.findall('\d*,?\d+', value)
    return clean
    
def get_today(value):
    clean = re.findall('\d+', value)
    return clean

def namify(value):
    return value.split('/')[-1]

class GithubTrendingItem(scrapy.Item):
    name = scrapy.Field(
        input_processor = MapCompose(namify),
        output_processor = TakeFirst(),
    )
    link = scrapy.Field(
        input_processor = MapCompose(make_link),
        output_processor = TakeFirst(),
    )
    description = scrapy.Field(
        input_processor = MapCompose(strip),
        output_processor = TakeFirst(),
    )
    language = scrapy.Field(
        output_processor = TakeFirst(),
    )
    total_stars = scrapy.Field(
        input_processor = MapCompose(strip, get_stars),
        output_processor = TakeFirst(),
    )
    stars_today = scrapy.Field(
        input_processor = MapCompose(strip, get_today),
        output_processor = TakeFirst(),
    )
    contributors = scrapy.Field()
    
    date = scrapy.Field(
        output_processor = TakeFirst(),
    )