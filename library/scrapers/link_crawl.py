import re

from bs4 import BeautifulSoup
import requests


class Website:
    """Basic info for website"""
    def __init__(self, name, url, target, abs_url, title_tag, body_tag):
        self.name = name
        self.url = url
        self.target = target
        self.abs_url = abs_url
        self.title_tag = title_tag
        self.body_tag = body_tag


class Content:
    """Harvested data content"""
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body

    def print(self):
        print(f'URL: {self.url}')
        print(f'Title: {self.title}')
        print(f'Body: {self.body}')


class Crawler:
    """Finds links on page"""
    def __init__(self, site):
        self.site = site
        self.visited = []

    def get_page(self, url):
        try:
            r = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(r.text, 'html.parser')

    def safe_get(self, page_obj, selector):
        elements = page_obj.select(selector)
        if elements is not None and len(elements) > 0:
            return '\n'.join([e.get_text() for e in elements])
        return ''

    def parse(self, url):
        soup = self.get_page(url)
        if soup is not None:
            title = self.safe_get(soup, self.site.title_tag)
            print(title)
            body = self.safe_get(soup, self.site.body_tag)
            print(body)
            if title != '' and body != '':
                content = Content(url, title, body)
                content.print()

    def crawl(self):
        soup = self.get_page(self.site.url)
        target_pages = soup.find_all('a', 
                href=re.compile(self.site.target)
        )
        for page in target_pages:
            page = page.attrs['href']
            print(page)
            if page not in self.visited:
                self.visited.append(page)
                if not self.site.abs_url:
                    page = f'{self.site.url}{page}'
                self.parse(page)


corey = Website('Corey', 'https://coreyms.com/', '(/category/development/)',
                  True, 'h1', 'div.entry-content')
crawler = Crawler(corey)
crawler.crawl()