from bs4 import BeautifulSoup

with open('info.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

rows = soup.find('table').find_all('tr')[1:]

# table data
table_data = []
for row in rows:
    td = row.find_all('td')
    email = td[1].text
    number = td[2].text

    data = {
        'email': email,
        'number': number,
    }
    table_data.append(data)


# special table
special_data = []
special = soup.find('div', class_='special_table')
for tr in special.find_all('tr')[1:]:
    values = [td.text for td in tr.find_all('td')]
    if values:
            
        data = {
            'email': values[1],
            'number': values[2],
        }
        special_data.append(data)


# combine the two lists 
all_data = table_data + special_data


# do it all in one swoop
for tr in soup.find_all('tr'):
    values = [td.text for td in tr.find_all('td')]
    if len(values) != 0:
        data = {
            'email': values[1],
            'number': values[2],
        }
