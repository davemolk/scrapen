from bs4 import BeautifulSoup
import requests

import datetime
import random
import re


random.seed()
def get_links(url):
    try:
        r  = requests.get(f'https://en.wikipedia.org{url}', timeout=5)
        r.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise SystemExit(e) 
    soup = BeautifulSoup(r.text, 'html.parser')
    links = soup.find('div', id='bodyContent').find_all(
        'a', href=re.compile(r'^(/wiki/)((?!:).)*$'))
    if len(links) == 0:
        return None
    else:  
        return soup.find('div', id='bodyContent').find_all(
            'a', href=re.compile(r'^(/wiki/)((?!:).)*$'))

    
links = get_links('/wiki/Kevin_Bacon')
while len(links) > 0:
    new_article = links[random.randint(0, len(links)-1)].attrs['href']
    print(new_article)
    links = get_links(new_article)


