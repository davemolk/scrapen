# parameters
url, callback, method, meta, body, headers, cookies, encoding, priority, dont_filter, errback, flags, cb_kwargs


# Request.meta special keys
The Request.meta attribute can contain any arbitrary data, but there are some special keys recognized by Scrapy and its built-in extensions. Some good stuff here


# request object
you can return (yield) multiple times within a function
def parse(self, response):
    for h3 in response.css('h3').getall():
        yield {"title": h3}

    for href in response.css('a::attr(href)').getall():
        yield scrapy.Request(response.urljoin(href), self.parse)

