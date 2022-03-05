import scrapy


class Write(scrapy.Spider):
    name = 'c'
    allowed_domains = ['quotes.toscrape.com']
    start_urls=['https://quotes.toscrape.com']

    def parse(self, response):
        author_links = response.css('small.author + a::attr(href)')
        yield from response.follow_all(author_links, self.parse_author)

        next = response.css('li.next a::attr(href)').get()
        if next is not None:
            yield response.follow(next, self.parse)
        # pagination = response.css('li.next a')
        # yield from response.follow_all(pagination, self.parse)

    def parse_author(self, response):
        name = response.css('h3.author-title::text').get(default='').strip()
        dob = response.css('span.author-born-date::text').get()

        yield {
            "name": name,
            "dob": dob,
        }