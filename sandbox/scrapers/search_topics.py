from bs4 import BeautifulSoup
import requests


class Content:
    """Base class for articles/pages"""

    def __init__(self, topic, url, title, body):
        self.topic = topic
        self.url = url
        self.title = title
        self.body = body
        

    def print(self):
        """Printing function"""
        print(f'New article found for {self.topic}:')
        print(f'URL: {self.url}')
        print(f'Title: {self.title}')
        print(f'Body: \n{self.body}')
        

class Website:
    """Info for website structure"""

    def __init__(self, name, url, search_url, result_listing,
                result_url, abs_url, title_tag, body_tag):
        self.name = name
        self.url = url
        self.search_url = search_url
        self.result_listing = result_listing
        self.result_url = result_url
        self.abs_url = abs_url
        self.title_tag = title_tag
        self.body_tag = body_tag


class Crawler:
    """Harvest links from site search functionality"""

    def get_page(self, url):
        try:
            r = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(r.text, 'html.parser')

    def get_safe(self, page_obj, selector):
        """Given a selector, search for object"""
        child_obj = page_obj.select(selector)
        if child_obj is not None and len(child_obj) > 0:
            return child_obj[0].get_text()
        print('*** unable to find element ***')
        return ""

    def search(self, topic, site):
        """Searches site for a given topic"""
        soup = self.get_page(site.search_url + topic)
        search_results = soup.select(site.result_listing)
        for result in search_results:
            url = result.select(site.result_url)[0].attrs['href']
            if site.abs_url:
                soup = self.get_page(url)
            else:
                soup = self.get_page(site.url + url)
            if soup is None:
                print('Problem with site or url. Moving on...')
                return
            title = self.get_safe(soup, site.title_tag)
            body = self.get_safe(soup, site.body_tag)
            if title != '' and body != '':
                content = Content(topic, url, title, body)
                content.print()
    

crawler = Crawler()

site_data = [
    # ['Reuters', 'http://reuters.com', 'http://www.reuters.com/search/news?blob=', 
    #     'div.search-result-content', 'h3.search-result-title a', False, 'h1', 
    #     'div.StandardArticleBody_body_1gnLA'],
    # ['Brookings', 'http://www.brookings.edu', 'https://www.brookings.edu/search/?s=',
    #     'div.list-content article', 'h4.title a', True, 'h1', 'div.post-body'],
    ['Corey', 'https://coreyms.com', 'https://coreyms.com/?s=', 'main.content article', 
            'h2.entry-title a', True, 'h1', 'div.entry-content']
]

sites = []
for row in site_data:
    sites.append(Website(row[0], row[1], row[2], row[3], row[4],
                        row[5], row[6], row[7]
    ))
topics = ['python', 'regex',]
for topic in topics:
    print(f'Getting info about {topic}')
    print()
    for site in sites:
        crawler.search(topic, site)


