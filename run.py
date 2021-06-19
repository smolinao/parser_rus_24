import random

from bs4 import BeautifulSoup
from requests_html import HTMLSession
import re


session = HTMLSession()
response = session.get('https://russia24.pro/')
soup = BeautifulSoup(response.content, 'html.parser')

items = soup.find_all('div', class_='r24_item')


def save_text_to_file(text):
    my_file = open("{}.txt".format(random.randint(1, 10000)), "w+")
    my_file.write(text)
    my_file.close()


def get_text_from_post(_url):
    _session = HTMLSession()
    text = _session.get(_url).text
    r = re.compile('(?<=<p>).*?(?=<\/p>)')
    result = re.findall(r, text)
    content = ''
    for result_string in result[0:len(result)-3]:
        content += result_string
    data_r = BeautifulSoup(content, 'html.parser')
    return data_r.text


if __name__ == '__main__':
    data_string = ''
    for i in items:
        item = i.find('a', href=True)
        itemName = item.find('h3').text.strip()
        # item_city = item.find('div', class_='r24Label r24_city')  TODO если нужен город
        print('{}'.format(itemName))
        print(get_text_from_post(item['href']))

        data_string += "{}:\r\n{}\r\n\r\n".format(itemName, get_text_from_post(item['href']))
    save_text_to_file(data_string)
