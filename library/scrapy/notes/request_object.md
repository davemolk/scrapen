# request object
you can return (yield) multiple times within a function
def parse(self, response):
    for h3 in response.css('h3').getall():
        yield {"title": h3}

    for href in response.css('a::attr(href)').getall():
        yield scrapy.Request(response.urljoin(href), self.parse)

