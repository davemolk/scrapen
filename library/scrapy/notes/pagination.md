# pagination
option 1
next_page = response.css('ul.page-numbers a.next::attr(href)').get()
    if next_page is not None:
        yield response.follow(next_page, callback=self.parse)


option 2
next_page = response.css('ul.page-numbers a.next::attr(href)').get()
    if next_page is not None:
        next_page = response.urljoin(next_page)
        yield scrapy.Request(next_page, callback=self.parse)

