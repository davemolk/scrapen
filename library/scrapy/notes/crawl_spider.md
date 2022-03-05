# CrawlSpider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

need to set rules and can't name your parse function 'parse'

rules are always a tuple and you don't need to specify a callback function for the first rule...scrapy will automatically follow those urls
