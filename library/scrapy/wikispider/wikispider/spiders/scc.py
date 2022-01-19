import re
import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Benevolent_dictator_for_life'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

all = soup.find_all('a')
# print(all)

filtered = soup.find_all('a', href=re.compile(r'^(/wiki/)((?!:).)*$'))
print(filtered)