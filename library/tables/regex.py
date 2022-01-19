from bs4 import BeautifulSoup
import pandas as pd


import re


with open('info.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')


# just regex
email = re.findall(r'([\d\w\-\.]+@[\d\w\-\.]+\.\w+)', soup.text)
phone_numbers = re.findall(r'1-[\d]{3}-[\d]{3}-[\d]{4}', soup.text)


# regex and soup
soup_email = soup.find_all('td', string=re.compile(r'([\d\w\-\.]+@[\d\w\-\.]+\.\w+)'))
cleaned_email = [email.text for email in soup_email]


soup_phone = soup.find_all('td', string=re.compile(r'1-[\d]{3}-[\d]{3}-[\d]{4}'))
cleaned_phone = [phone.text for phone in soup_phone]

df = pd.DataFrame(cleaned_email)
df.to_csv('emails.csv', index=False)

df = pd.DataFrame(cleaned_phone)
df.to_csv('phone.csv', index=False)