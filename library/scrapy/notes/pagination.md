# pagination
option 1
next_page = response.css('ul.page-numbers a.next::attr(href)').get()
    if next_page is not None:
        # response.follow supports relative URLs, so we don't need to use response.urljoin
        yield response.follow(next_page, callback=self.parse)


option 1a
pagination = response.css('li.next a')
yield from response.follow_all(pagination, self.parse)


option 2
next_page = response.css('ul.page-numbers a.next::attr(href)').get()
    if next_page is not None:
        # Request requires absolute URLs, so we need response.urljoin
        next_page = response.urljoin(next_page)
        yield scrapy.Request(next_page, callback=self.parse)



response.follow will use href attribute automatically, so can write
for href in response.css('ul.pager a::attr(href)'):
    yield response.follow(href, callback=self.parse)

as

for a in response.css('ul.pager a'):
    yield response.folow(a, callback=self.parse)


# iterate over multiple with response.follow_all
anchors = response.css('ul.pager a')
yield from response.follow_all(anchors, callback=self.parse)

or 

yield from response.follow_all(css='ul.pager a', callback=self.parse)