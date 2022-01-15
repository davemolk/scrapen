# commands
scrapy startproject <projectname>
scrapy genspider <spider name> <allowed_domains>


# shell commands
scrapy shell <url you want to look at>
scrapy shell -s USER_AGENT='' <url>

can also let shell load and then use fetch(<url>) to get the page

>>> response

>>> response.css('div.image_container a::attr(href)').get() # gets first

could also write response.css('div.image_container a').attrib['href'] to get the link href

clean data with .strip(), .replace(), etc.


# css selectors
access other attributes like so: response.css('a[title='Next']::attr(href)')


# item
go to items.py

enter fields (name = scrapy.Field())

next, import the class into your spider
(from book_pages.items import BookPagesItem)

instantiate item within your parse function, define its values via css, then yield item


# item loader
within items.py

from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags

then import ItemLoader into the spider


# crawl
scrapy crawl <name>


# output data
scrapy crawl <name> -o books.csv
scrapy crawl <name> -o books.json

-o will append and -O will overwrite