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


# logging settings
LOG_FILE
LOG_FILE_APPEND
LOG_ENABLED
LOG_ENCODING
LOG_LEVEL
LOG_FORMAT
LOG_DATEFORMAT
LOG_STDOUT
LOG_SHORT_NAMES

The first couple of settings define a destination for log messages. If LOG_FILE is set, messages sent through the root logger will be redirected to a file named LOG_FILE with encoding LOG_ENCODING. If unset and LOG_ENABLED is True, log messages will be displayed on the standard error. If LOG_FILE is set and LOG_FILE_APPEND is False, the file will be overwritten (discarding the output from previous runs, if any). Lastly, if LOG_ENABLED is False, there won’t be any visible log output.

LOG_LEVEL determines the minimum level of severity to display, those messages with lower severity will be filtered out. It ranges through the possible levels listed in Log levels.

LOG_FORMAT and LOG_DATEFORMAT specify formatting strings used as layouts for all messages. Those strings can contain any placeholders listed in logging’s logrecord attributes docs and datetime’s strftime and strptime directives respectively.

If LOG_SHORT_NAMES is set, then the logs will not display the Scrapy component that prints the log. It is unset by default, hence logs contain the Scrapy component responsible for that log output.