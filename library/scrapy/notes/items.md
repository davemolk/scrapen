# item loader
within items.py

from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags

then import ItemLoader into the spider


# items.py
go to items.py

enter fields (name = scrapy.Field())

next, import the class into your spider
(from book_pages.items import BookPagesItem)

instantiate item within your parse function, define its values via css, then yield item
