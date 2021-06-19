from bs4 import BeautifulSoup
from requests_html import HTMLSession


session = HTMLSession()
response = session.get('https://russia24.pro/')
soup = BeautifulSoup(response.content, 'html.parser')

items = soup.find_all('div', class_='r24_item')


for i in items:
    item = i.find('a', href=True)
    itemName = item.find('h3').text.strip()
    item_city = item.find('div', class_='r24Label r24_city')
    if item_city:
        print('city: {}\r\n{} -> {}\r\n'.format(item_city.text.strip(), itemName, item['href']))
    else:
        print('{} -> {}\r\n'.format(itemName, item['href']))


