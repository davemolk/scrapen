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

The view(response) command let’s us view the response our shell or later our spider receives from the server.


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

>>> response.css('.author + a') gets us this:
<a href="/author/Albert-Einstein">(about)</a>

(html, we're using adjacent sibling selector:)
<small class='author' itemprop='author'>Albert Einstein</small><a href="/author/Albert-Einstein">(about)</a>


# css and regex
>>> response.css('title::text').re(r'Q\w+')
['Quotes']
>>> response.css('title::text').re(r'(\w+) to (\w+)')
['Quotes', 'Scrape']


# items.py
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


# yield and yield from
use yielf from for iterables

def parse(self, response):
        author_page_links = response.css('.author + a')
        yield from response.follow_all(author_page_links, self.parse_author)

or shorten further:
yield from response.follow_all(css='ul.pager a', callback=self.parse)


# crawl
scrapy crawl <name>


# pagination
option 1
next_page = response.css('ul.page-numbers a.next::attr(href)').get()
    if next_page is not None:
        yield response.follow(next_page, callback=self.parse)


option 2
next_page = response.css('ul.page-numbers a.next::attr(href)').get()
    if next_page is not None:
        next_page = response.urljoin(next_page)
        yield scrapy.Request(next_page, callback=self.parse)


# output data
scrapy crawl <name> -o books.csv
scrapy crawl <name> -o books.json

-o will append and -O will overwrite


# CrawlerProcess
use if you just want the spider and none of the other Scrapy goodness


# CrawlSpider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

need to set rules and can't name your parse function 'parse'

rules are always a tuple and you don't need to specifya callback function for the first rule...scrapy will automatically follow those urls


# pipelines
import sqlite3

create an init and connect to db 
def __init__(self):
    self.con = sqlite3.connect('mtiles.db') 
    # cursor is what we use to execute commands into db
    self.cur = self.con.cursor()


# cURL commands
https://michael-shub.github.io/curl2scrapy/


# logins
option 1)
get csrf value from network tab after a login attempt
from scrapy import FormRequest
csrf_token = response.xpath("//*[@name='csrf_token']/@value").get()
yield FormRequest.from_response(response, formdata, callback)

option 2)




# scrapy playwright
https://github.com/scrapy-plugins/scrapy-playwright

add to settings: DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}

TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"