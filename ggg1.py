from random import choice
import requests as re
from bs4 import BeautifulSoup
# from px_scrap import scrap_proxy
from proxyes2 import get_free_proxies
import pandas as pd

free_proxies = get_free_proxies()

desktop_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 '
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
HEADERS = {"user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0',
           'accept': '*/*'}


def random_headers():
    return {'User-Agent': choice(desktop_agents), 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,'
                                                            'image/webp,*/*;q=0.8'}


data = []
df = pd.DataFrame(free_proxies)
print(df)
for rec in df:
    url = 'https://www.avito.ru/murmanskaya_oblast/kvartiry/prodam-ASgBAgICAUSSA8YQ?cd=1&p=13'
    r = re.get(url, headers=random_headers())
    soup = BeautifulSoup(r.text, 'lxml')
    print(r.text)
    if r.status_code == 200:
        s = soup.findAll('div', class_='iva-item-root-_lk9K photo-slider-slider-S15A_ iva-item-list-rfgcH '
                                       'iva-item-redesign-rop6P iva-item-responsive-_lbhG iva-item-ratingsRedesign-ydZfp '
                                       'items-item-My3ih items-listItem-Gd1jN js-catalog-item-enum')
        print(len(s))
        for i in s:
            if  i.find('span', class_='geo-address-fhHd0 text-text-LurtD text-size-s-BxGpL') == None:
                addr = ''
            else:
                addr = i.find('span', class_='geo-address-fhHd0 text-text-LurtD text-size-s-BxGpL').find(
                    'span').get_text()
                print(addr)
    else:
        print('А не работает')

