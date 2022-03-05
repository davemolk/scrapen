# yield and yield from
use yield from for iterables

def parse(self, response):
        author_page_links = response.css('.author + a')
        yield from response.follow_all(author_page_links, self.parse_author)

or shorten further:
yield from response.follow_all(css='ul.pager a', callback=self.parse)