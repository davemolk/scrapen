# logins
option 1)
get csrf value from network tab after a login attempt
from scrapy import FormRequest
csrf_token = response.xpath("//*[@name='csrf_token']/@value").get()
yield FormRequest.from_response(response, formdata, callback)

option 2)
look for form inputs and populate formdata from there (essentially consolidates the two steps from option 1 into 1 step)

option 3) 
use def start_requests and return the populated FormRequest object




import scrapy

def authentication_failed(response):
    # TODO: Check the contents of the response and return True if it failed
    # or False if it succeeded.
    pass

class LoginSpider(scrapy.Spider):
    name = 'example.com'
    start_urls = ['http://www.example.com/users/login.php']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'username': 'john', 'password': 'secret'},
            callback=self.after_login
        )

    def after_login(self, response):
        if authentication_failed(response):
            self.logger.error("Login failed")
            return

        # continue scraping with authenticated session...