import scrapy

import re

class GetEmail(scrapy.Spider):
    name = 'e'

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Safari/537.36',
        }

    def __init__(self, url=None, *args, **kwargs):
        super(GetEmail, self).__init__(*args, **kwargs)
        self.allowed_domains = [f'{url}']
        self.start_urls = [f'https://{url}']
        self.total_emails = 0

    def parse(self, response):
        for link in response.css('a::attr(href)'):
            link = response.urljoin(link.get())
            yield scrapy.Request(link,
                                self.parse_details)

    def parse_details(self, response):
        emails = re.findall(r'([\w\-\.]+@[A-Za-z][\w\-\.]+\.\w+)', response.text)
        for e in emails:
            self.total_emails += 1
            print('email total: ', self.total_emails)
            yield {
                'url': response.url,
                'email': e
            }

        # tweak above regex and handle name [at] domain and similar instances
        # use an item for storage