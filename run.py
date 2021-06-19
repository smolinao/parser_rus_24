from bs4 import BeautifulSoup
from requests_html import HTMLSession
import re


session = HTMLSession()
response = session.get('https://russia24.pro/')
soup = BeautifulSoup(response.content, 'html.parser')

items = soup.find_all('div', class_='r24_item')


def get_text_from_post(_url):
    _session = HTMLSession()
    text = _session.get(_url).text
    r = re.compile('(?<=<p>).*?(?=<\/p>)')
    result = re.findall(r, text)[2]
    data_r = BeautifulSoup(result, 'html.parser')
    return data_r.text


for i in items:
    item = i.find('a', href=True)
    itemName = item.find('h3').text.strip()
    item_city = item.find('div', class_='r24Label r24_city')
    if item_city:
        print('city: {}\r\n{}'.format(item_city.text.strip(), itemName))
        print(get_text_from_post(item['href']))
    else:
        print('{}'.format(itemName))
        print(get_text_from_post(item['href']))


