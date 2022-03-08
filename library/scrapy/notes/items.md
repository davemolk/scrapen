# items.py
// items.py

import scrapy

class Product(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()
    tags = scrapy.Field()
    last_updated = scrapy.Field(serializer=str)

next, import the class into your spider
(from book_pages.items import BookPagesItem)

instantiate item within your parse function, define its values via css, then yield item


# working with items (same as how you work with dictionaries)
product = Product(name='Desktop PC', price=1000)
product['price'] = 750
product.get('last_updated', 'default value')
product.keys()
product.values()
product.items()


# dataclass
dataclass() allows defining item classes with field names, so that item exporters can export all fields by default even if the first scraped object does not have values for all of them. Can also type item fields, although these aren't enforced at runtime.

from dataclasses import dataclass
 
@dataclass
class CustomItem:
    one_field: str
    second_field: int


# item loader
items provide the container of scraped data, while Item Loaders provide the mechanism for populating that container.

// items.py
from itemloaders.processors import TakeFirst, MapCompose, Join
from scrapy.loader import ItemLoader

class ProductLoader(ItemLoader):

    default_output_processor = TakeFirst()

    name_in = MapCompose(str.title)
    name_out = Join()

    price_in = MapCompose(str.strip)


// import ItemLoader into the spider

from scrapy.loader import ItemLoader
from myproject.items import Product

def parse(self, response):
    l = ItemLoader(item=Product(), response=response)
    l.add_xpath('name', '//div[@class="product_name"]')
    l.add_xpath('name', '//div[@class="product_title"]')
    l.add_xpath('price', '//p[@id="price"]')
    l.add_css('stock', 'p#stock')
    l.add_value('last_updated', 'today') # you can also use literal values
    return l.load_item()


Note: could also process in field definitions, like so:
import scrapy
from itemloaders.processors import Join, MapCompose, TakeFirst
from w3lib.html import remove_tags

def filter_price(value):
    if value.isdigit():
        return value

class Product(scrapy.Item):
    name = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=Join(),
    )
    price = scrapy.Field(
        input_processor=MapCompose(remove_tags, filter_price),
        output_processor=TakeFirst(),
    )


# common processors (https://itemloaders.readthedocs.io/en/latest/built-in-processors.html)
Compose: A processor which is constructed from the composition of the given functions. This means that each input value of this processor is passed to the first function, and the result of that function is passed to the second function, and so on, until the last function returns the output value of this processor.

>>> from itemloaders.processors import Compose
>>> proc = Compose(lambda v: v[0], str.upper)
>>> proc(['hello', 'world'])
'HELLO'


Join: Returns the values joined with the separator given in the __init__ method, which defaults to ' '. It doesn’t accept Loader contexts. When using the default separator, this processor is equivalent to the function: ' '.join

>>> from itemloaders.processors import Join
>>> proc = Join()
>>> proc(['one', 'two', 'three'])
'one two three'
>>> proc = Join('<br>')
>>> proc(['one', 'two', 'three'])
'one<br>two<br>three'


MapCompose: The input value of this processor is iterated and the first function is applied to each element. The results of these function calls (one for each element) are concatenated to construct a new iterable, which is then used to apply the second function, and so on, until the last function is applied to each value of the list of values collected so far. The output values of the last function are concatenated together to produce the output of this processor.

>>> def filter_world(x):
...     return None if x == 'world' else x
...
>>> from itemloaders.processors import MapCompose
>>> proc = MapCompose(filter_world, str.upper)
>>> proc(['hello', 'world', 'this', 'is', 'something'])
['HELLO', 'THIS', 'IS', 'SOMETHING']


TakeFirst: Returns the first non-null/non-empty value from the values received, so it’s typically used as an output processor to single-valued fields.

>>> from itemloaders.processors import TakeFirst
>>> proc = TakeFirst()
>>> proc(['', 'one', 'two', 'three'])
'one'