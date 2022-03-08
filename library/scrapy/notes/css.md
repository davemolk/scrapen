# css selectors
access other attributes like so: response.css('a[title='Next']::attr(href)')

>>> response.css('.author + a') gets us this:
<a href="/author/Albert-Einstein">(about)</a>

(html, we're using adjacent sibling selector:)
<small class='author' itemprop='author'>Albert Einstein</small><a href="/author/Albert-Einstein">(about)</a>


# setting defaults
>>> response.css('div.author::text').get(default='not found')
'not found'

use defaults if you always want a string (response.css('img::text').getall() returns
None if there is no text, so response.css('img::text').getall(default='not found'))


# css and regex
>>> response.css('title::text').re(r'Q\w+')
['Quotes']
>>> response.css('title::text').re(r'(\w+) to (\w+)')
['Quotes', 'Scrape']


# single element
you can chain attrib if you're expecting just one element 
(you can call this on a list but it will grab just the first element)

>>> response.css('img').attrib['src'] (need 'src' in this case)


This is really helpful if you want to write Python instead of relying on selectors:

>>> [a.attrib['href'] for a in response.css('a')]
['image1.html', 'image2.html', 'image3.html', 'image4.html', 'image5.html']

