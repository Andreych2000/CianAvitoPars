import requests as re
from bs4 import BeautifulSoup
from random import choice
from random import randint
from time import sleep
import json

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
URL = 'https://www.cian.ru/cat.php?deal_type=sale&engine_version=2&object_type%5B0%5D=3&offer_type=suburban&region=4594'
HOST = 'https://www.cian.ru'
data = []
def random_headers():
    return {'User-Agent': choice(DESKTOP_AGENTS),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}

ro = re.get(URL, headers=random_headers())
print(ro.status_code)
print(ro.text)
so = BeautifulSoup(ro.text, 'html.parser')

pg = len(so.find_all('div', class_='_93444fe79c--wrapper--bKcEk').find_all('a', class_='_93444fe79c--list-itemLink--BU9w6'))
print(pg+1)
for p in range(1, int(pg)+1):
    print(p)
    url = f"https://murmansk.cian.ru/cat.php?deal_type=sale&engine_version=2&object_type%5B0%5D=3&offer_type=suburban&p={p}&region=4594"
    r = re.get(url, headers=random_headers())
    print(url)
    # генерим случайное число
    sl = randint(5, 30)
    print(sl)
    sleep(sl)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        s = soup.findAll('article', class_='_93444fe79c--container--Povoi _93444fe79c--cont--OzgVc')
        print(len(s))
        sl = randint(5, 10)
        print('slPL' + ' - ' + str(sl))
    # sleep(sl)