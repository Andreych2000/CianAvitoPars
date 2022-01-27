from random import choice
import requests as re
from bs4 import BeautifulSoup
from proxybroker import Broker
import asyncio

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


def random_headers():
    return {'User-Agent': choice(desktop_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
#####################################################################
async def save(proxies, filename):
    with open(filename, 'w') as f:
        while True:
            proxy = await proxies.get()
            if proxy is None:
                break
            row = f'{proxy.host}:{proxy.port}\n'
            f.write(row)


def get_proxies(limit=1000):
    proxies = asyncio.Queue()
    broker = Broker(proxies)
    tasks = asyncio.gather(broker.grab(limit=limit),
                           save(proxies, filename='proxies.txt'))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(tasks)
#####################################################################

url = 'https://murmansk.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=flat&region=4594&room1=1&room2=1' \
      '&room3=1&room4=1&room5=1&room6=1&room7=1&room9=1 '
r = re.get(url, headers=random_headers(), proxies=get_proxies())
print(r.text)
soup = BeautifulSoup(r.text, 'lxml')
data = []
###############################################################################################
s = soup.findAll('article', class_='_93444fe79c--container--Povoi _93444fe79c--cont--OzgVc')
print(len(s))
for i in s:
    link = i.find(
        'a', class_='_93444fe79c--link--eoxce'
    ).get('href')
    # print(link)
    gg = i.find('div', class_='_93444fe79c--labels--L8WyJ').findAll('a', class_='_93444fe79c--link--NQlVc')
    # print(len(gg))
    addres0 = i.find('div', class_='_93444fe79c--labels--L8WyJ').findAll('a', class_='_93444fe79c--link--NQlVc')[0].text
    addres1 = i.find('div', class_='_93444fe79c--labels--L8WyJ').findAll('a', class_='_93444fe79c--link--NQlVc')[1].text
    addres2 = i.find('div', class_='_93444fe79c--labels--L8WyJ').findAll('a', class_='_93444fe79c--link--NQlVc')[2].text
    if len(gg) >= 4:
        addres3 = i.find('div', class_='_93444fe79c--labels--L8WyJ').findAll('a', class_='_93444fe79c--link--NQlVc')[
            3].text
    else:
        addres3 = ''
    if len(gg) >= 5:
        addres4 = i.find('div', class_='_93444fe79c--labels--L8WyJ').findAll('a', class_='_93444fe79c--link--NQlVc')[
            4].text
    else:
        addres4 = ''
    if len(gg) >= 6:
        addres5 = i.find('div', class_='_93444fe79c--labels--L8WyJ').findAll('a', class_='_93444fe79c--link--NQlVc')[
            5].text
    else:
        addres5 = ''
    r1 = re.get(link, headers=random_headers())
    soup1 = BeautifulSoup(r1.text, 'lxml')
    items = soup1.findAll('div', class_='a10a3f92e9--offer_card_page-center--DIv6H')
    for item in items:
        h1 = item.find('h1', class_='a10a3f92e9--title--UEAG3')
        total_area = item.find('div', class_='a10a3f92e9--info-value--bm3DC')
        print(total_area.text)
    data.append(dict(link=link, titl=h1.text,
                     addres=addres0 + ' ' + addres1 + ' ' + addres2 + ' ' + addres3 + ' ' + addres4 + ' ' + addres5,
                     total_area=total_area.text))
print(data)
