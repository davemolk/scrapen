# arguments
pass through crawl command using the -a option
scrapy crawl <spider_name> -a category=electronics
(access via __init__)
def __init__(self, category=None, *args, **kwargs):
    super.(MySpider, self).__init__(*args, **kwargs)
    self.start_urls = [f'http://www.example.com/categories/{category}']

note: could also write as:
def start_requests(self):
    yield scrapy.Request(f'http://www.example.com/categories/{self.category})


A valid use case is to set the http auth credentials used by HttpAuthMiddleware or the user agent used by UserAgentMiddleware:

scrapy crawl myspider -a http_user=myuser -a http_pass=mypassword -a user_agent=mybot

