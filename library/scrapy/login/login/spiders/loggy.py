import scrapy
from scrapy import FormRequest


class LoggySpider(scrapy.Spider):
    name = 'loggy'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/login']

    def parse(self, response):
        csrf_token = response.xpath("//*[@name='csrf_token']/@value").get()
        print(csrf_token)
        formdata = {
            'csrf_token': csrf_token,
            'username': 'scrapy',
            'password': 'gethappy',
        }
        yield FormRequest.from_response(
            response, 
            formdata=formdata, 
            callback=self.parse_after_login,
        )

    def parse_after_login(self, response):
        logout = response.css("a[href='/logout']").get()
        print("****************************************")
        print("printing logout:", logout)
