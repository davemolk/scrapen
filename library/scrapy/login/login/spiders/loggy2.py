import scrapy
from scrapy import FormRequest


class LoggySpider(scrapy.Spider):
    name = 'loggy2'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/login']

    def parse(self, response):
        inputs = response.css('form input')
        print(inputs)

        formdata = {}
        for input in inputs:
            name = input.css('::attr(type)').get()
            value = input.css('::attr(value)').get()
            formdata[name] = value
        
        print("*****formdata*****", formdata)
        formdata['username'] = 'loggy2'
        formdata['password'] = 'test1234'

        yield FormRequest.from_response(
            response,
            formdata = formdata,
            callback = self.parse_after_login,
        )
        
    def parse_after_login(self, response):
        logout = response.css("a[href='/logout']").get()
        print("****************************************")
        print("printing logout:", logout)
