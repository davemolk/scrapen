# css and regex
>>> response.css('title::text').re(r'Q\w+')
['Quotes']
>>> response.css('title::text').re(r'(\w+) to (\w+)')
['Quotes', 'Scrape']


# css selectors
access other attributes like so: response.css('a[title='Next']::attr(href)')

>>> response.css('.author + a') gets us this:
<a href="/author/Albert-Einstein">(about)</a>

(html, we're using adjacent sibling selector:)
<small class='author' itemprop='author'>Albert Einstein</small><a href="/author/Albert-Einstein">(about)</a>
