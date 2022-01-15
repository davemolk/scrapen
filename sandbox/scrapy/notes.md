# commands
scrapy startproject <projectname>
scrapy genspider <spider name> <allowed_domains>

# shell commands
scrapy shell <url you want to look at>
scrapy shell -s USER_AGENT='' <url>

>>> response

>>> response.css('div.image_container a::attr(href)').get() # gets first

# crawl
scrapy crawl <name>