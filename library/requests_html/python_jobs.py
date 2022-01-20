import pandas as pd
from requests_html import HTMLSession

import logging

logging.basicConfig(filename='book.log', level=logging.DEBUG,
                    format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')


class Scraper:
    def __init__(self):
        self.session = HTMLSession()
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
        self.url = 'https://realpython.github.io/fake-jobs/'

    def get_data(self):
        try:
            r = self.session.get(self.url)
        except Exception as err:
            logging.warning(err)
        if not r.html.find('div.column'):
            return False
        return r.html.find('div.column')

    def parse(self, data):
        jobs = []
        for job in data:
            title = job.find('h2.title', first=True).text
            company = job.find('h3.company', first=True).text
            location = job.find('p.location', first=True).text.strip()
            link = job.find('a')[1].attrs['href']
            item = {
                'title': title,
                'company': company,
                'location': location,
                'link': link,
            }
            jobs.append(item)
            logging.info(item)
        return jobs

    def save(self, results):
        df = pd.DataFrame(results)
        df.to_csv('python_jobs.csv', index=False)

if __name__ == '__main__':
    scrape = Scraper()
    data = scrape.get_data()
    if data:
        results = scrape.parse(data)
        scrape.save(results)
    else:
        print('an error occurred, please see log')