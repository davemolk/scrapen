import scrapy
from scrapy import FormRequest


class LoggySpider(scrapy.Spider):
    name = 'loggy3'
    allowed_domains = ['quotes.toscrape.com']

    def start_requests(self):
        return [scrapy.FormRequest('https://quotes.toscrape.com/login',
                                    formdata={'username': 'loggy3', 'password': 'test1234'},
                                    callback=self.parse_after_login)]
        
    def parse_after_login(self, response):
        logout = response.css("a[href='/logout']").get()
        print("****************************************")
        print("printing logout:", logout)
