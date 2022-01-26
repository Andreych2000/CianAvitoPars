from random import choice
import requests as re
from bs4 import BeautifulSoup

desktop_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0']

def random_headers():
    return {'User-Agent': choice(desktop_agents), 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}

# url = 'https://www.kinopoisk.ru/lists/top250/'
#
# r = re.get(url, headers=random_headers())
# soup = BeautifulSoup(r.text, 'lxml')
# s = "https://www.kinopoisk.ru/lists/top250/"+soup.find('div', class_='desktop-rating-selection-film-item').find('a', class_='selection-film-item-meta__link').get('href')
# # print(soup)
# print(s)
url = 'https://murmansk.cian.ru/kupit-kvartiru-1-komn-ili-2-komn/'
r = re.get(url, headers=random_headers())
soup = BeautifulSoup(r.text, 'lxml')
# s = soup.find(
#     'article', class_='_93444fe79c--container--Povoi _93444fe79c--cont--OzgVc').find(
#     'div', class_='_93444fe79c--content--lXy9G').find('a', class_='_93444fe79c--link--eoxce').get('href')
# print(s)
s = soup.findAll('article', class_='_93444fe79c--container--Povoi _93444fe79c--cont--OzgVc')
print(len(s))
for s in s:
    link = soup.find(
        'article', class_='_93444fe79c--container--Povoi _93444fe79c--cont--OzgVc'
    ).find(
        'a', class_='_93444fe79c--link--eoxce'
    ).find(
    'div', class_='_93444fe79c--content--lXy9G')#.get('href')
    print(link)