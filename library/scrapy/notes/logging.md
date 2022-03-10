scrapy.log has been deprecated in favor of the Python logging

logging.CRITICAL - for critical errors (highest severity)
logging.ERROR - for regular errors
logging.WARNING - for warning messages
logging.INFO - for informational messages
logging.DEBUG - for debugging messages (lowest severity)

# examples
import logging
logging.warning("this is a warning")


On top of that, you can create different “loggers” to encapsulate messages. (For example, a common practice is to create different loggers for every module). These loggers can be configured independently, and they allow hierarchical constructions.


# customize loggers
import logging
logger = logging.getLogger()
logger.warning("This is a warning")

logger2 = logging.getLogger('my_custom_logger')


# within spiders
import scrapy

class MySpider(scrapy.Spider):

    name = 'myspider'
    start_urls = ['https://scrapy.org']

    def parse(self, response):
        self.logger.info('Parse function called on %s', response.url)


if you want to use your customized loggers, instantiate them outside of the class and refer from within:
import logging
import scrapy

logger = logging.getLogger('my_custom_logger')

class MySpider(scrapy.Spider):
    name = 'spidey'
    start_urls = ['https://scrapy.org']

    def parse(self, response):
        logger.info('parse function called on %s', response.url)