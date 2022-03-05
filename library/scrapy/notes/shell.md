# shell commands
scrapy shell <url you want to look at>
scrapy shell -s USER_AGENT='FAKEUSER' <url>

can also let shell load and then use fetch(<url>) to get the page

>>> response

>>> response.css('div.image_container a::attr(href)').get() # gets first

could also write response.css('div.image_container a').attrib['href'] to get the link href

clean data with .strip(), .replace(), etc. (if not using items.py or item loaders)

The view(response) command let’s us view the response our shell or later our spider receives from the server.


# shell headers
>>> response.headers (oh shit, I've been spottted as Scrapy)
>>> req = Request('https://httpbin.org/headers', headers={'User-Agent': 'FAKE USER'})


# shell no project
>>> scrapy shell
>>> from scrapy import Request
>>> req = Request('https://httpbin.org/headers')
>>> fetch(req)
>>> response
