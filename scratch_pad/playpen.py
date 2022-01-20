from bs4 import BeautifulSoup
import requests

url = 'https://www.pythonscraping.com/pages/page3.html'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

table = soup.find('table')
rows = table.find_all('tr', class_='gift')
for row in rows:
    data = row.find_all('td')
    info = {
        'name': data[0].text.strip(),
        'description': data[1].text.strip(),
        'price': data[2].text.strip(),
        'image': data[3].img['src'],
    }
    