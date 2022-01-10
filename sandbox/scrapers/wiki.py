import re

from bs4 import BeautifulSoup
import requests


pages = set()
def get_links(page_url):
    """Print title, first paragraph, and edit link"""
    
    global pages
    r = requests.get(f'http://en.wikipedia.org{page_url}')
    soup = BeautifulSoup(r.text, 'html.parser')
    try:
        print(soup.h1.get_text())
        print(soup.find(id='mw-content-text').find_all('p')[0])
        print(soup.find(id='ca-edit').find('span')
                .find('a').attrs['href'])
    except AttributeError:
        print(f'This page ({page_url} is missing something. Moving along...')
    for link in soup.find_all('a', href=re.compile(r'^(/wiki/)((?!:).)*$')):
        if 'href' in link.attrs and link.attrs['href'] not in pages:
            new_page = link.attrs['href']
            print('-' * 20)
            print(new_page)
            pages.add(new_page)
            get_links(new_page)

get_links('')
