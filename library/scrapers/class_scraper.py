from bs4 import BeautifulSoup
import requests


class Content:
    """Generalized content for crawler"""

    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body

    def print(self):
        """Print output"""
        print(f"url: {self.url}")
        print(f"title: {self.title}")
        print(f"body: {self.body}")


class Website:
    """General information about website structure"""

    def __init__(self, name, url, title_tag, body_tag):
        self.name = name
        self.url = url
        self.title_tag = title_tag
        self.body_tag = body_tag


class Crawler:
    """Generalized crawler"""

    def get_page(self, url):
        """Accepts url and returns soup object"""
        try:
            r = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(r.text, 'html.parser')

    def safe_get(self, page, selector):
        """
        Utility function used to get a content string from a
        Beautiful Soup object and a selector. Returns an empty 
        string if no object is found for the given selector.
        """
        elements = page.select(selector)
        if elements is not None and len(elements) > 0:
            return '\n'.join([element.text for element in elements])
        return ''

    def parse(self, site, url):
        """Parse soup object for given url"""
        soup = self.get_page(url)
        if soup is not None:
            title = self.safe_get(soup, site.title_tag)
            body = self.safe_get(soup, site.body_tag)
            if title != '' and body != '':
                content = Content(url, title, body)
                content.print()

crawler = Crawler()

site_data = [
    ['Reuters', 'http://reuters.com', 'h1', 'div.ArticleBodyWrapper'],
    ['Brookings', 'http://www.brookings.edu', 'h1', 'div.post-body'],
]
websites = []
for row in site_data:
    websites.append(Website(row[0], row[1], row[2],row[3]))


crawler.parse(
    websites[0], 'http://www.reuters.com/article/us-usa-epa-pruitt-idUSKBN19W2D0')
crawler.parse(
    websites[1],
    'https://www.brookings.edu/blog/techtank/2016/03/01/idea-to-retire-old-methods-of-policy-education/')
