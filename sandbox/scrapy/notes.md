# commands
scrapy startproject <projectname>
scrapy genspider <spider name> <allowed_domains>


# scrapy and bpython
pip3 install bpython and it will make scrapy's shell more user-friendly

can also use from pprint import pprint and then use pprint(response.headers) etc. for ease of readability


# shell commands
scrapy shell <url you want to look at>
scrapy shell -s USER_AGENT='FAKEUSER' <url>

can also let shell load and then use fetch(<url>) to get the page

>>> response

>>> response.css('div.image_container a::attr(href)').get() # gets first

could also write response.css('div.image_container a').attrib['href'] to get the link href

clean data with .strip(), .replace(), etc. (if not using items.py or item loaders)


# shell no project
>>> scrapy shell
>>> from scrapy import Request
>>> req = Request('https://httpbin.org/headers')
>>> fetch(req)
>>> response

pass in fake headers
>>> response.headers (oh shit, I've been spottted as Scrapy)
>>> req = Request('https://httpbin.org/headers', headers={'User-Agent': 'FAKE USER'})




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


# CrawlerProcess
use if you just want the spider and none of the other Scrapy goodness