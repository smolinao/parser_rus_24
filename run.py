import random

from bs4 import BeautifulSoup
from requests_html import HTMLSession
import re


class Parser:
    SESSION = HTMLSession()
    RESPONSE = SESSION.get('https://russia24.pro/')
    SOUP = BeautifulSoup(RESPONSE.content, 'html.parser')
    ITEMS = SOUP.find_all('div', class_='r24_item')

    @staticmethod
    def save_text_to_file(text):
        my_file = open("{}.txt".format(random.randint(1, 10000)), "w+")
        my_file.write(text)
        my_file.close()

    @staticmethod
    def get_text_from_post(_url):
        _session = HTMLSession()
        text = _session.get(_url).text
        r = re.compile('(?<=<p>).*?(?=<\/p>)')
        result = re.findall(r, text)
        content = ''
        for result_string in result[0:len(result) - 3]:
            content += result_string
        data_r = BeautifulSoup(content, 'html.parser')
        return data_r.text

    def _run(self):
        data_string = ''
        for i in self.ITEMS:
            item = i.find('a')
            itemName = item.find('h3').text.strip()
            # item_city = item.find('div', class_='r24Label r24_city')  TODO если нужен город
            print('{}'.format(itemName))
            print(self.get_text_from_post(item['href']))

            data_string += "{}:\r\n{}\r\n\r\n".format(itemName, self.get_text_from_post(item['href']))
        self.save_text_to_file(data_string)


if __name__ == '__main__':
    Parser()._run()
