import requests
from bs4 import BeautifulSoup
from random import choice

URL = 'https://murmansk.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=flat&region=4594&room1=1&room2=1' \
      '&room3=1&room4=1&room5=1&room6=1&room7=1&room9=1'
DESKTOP_AGENTS = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 '
                  'Safari/537.36',
                  'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 '
                  'Safari/537.36',
                  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/54.0.2840.99 Safari/537.36',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) '
                  'Version/10.0.1 Safari/602.2.14',
                  'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 '
                  'Safari/537.36',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/54.0.2840.98 Safari/537.36',
                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/54.0.2840.98 Safari/537.36',
                  'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 '
                  'Safari/537.36',
                  'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 '
                  'Safari/537.36',
                  'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0']



def random_headers():
    return {'User-Agent': choice(DESKTOP_AGENTS),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}

def get_html(url, params=None):
    r = requests.get(url, headers=random_headers(), params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.findAll('article', class_='_93444fe79c--container--Povoi _93444fe79c--cont--OzgVc')
    # items = soup.findAll('div', class_='_93444fe79c--card--ibP42 _93444fe79c--promoted--PnMmw')
    room = []
    for item in items:
        link = item.find('a', class_='_93444fe79c--link--eoxce').get('href')
        room.append({
            'link': link
        })
        print(room)


def parse():
    html = get_html(URL)
    print(html.status_code)
    if html.status_code == 200:
        # print(html.text)
        get_content(html.text)
    else:
        print('Error')
parse()
