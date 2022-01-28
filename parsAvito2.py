from random import choice
import requests as re
from bs4 import BeautifulSoup
from time import sleep
import json
import pdfkit

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
URL = 'https://www.avito.ru/murmanskaya_oblast/kvartiry/prodam-ASgBAgICAUSSA8YQ?cd=1'
host = 'https://www.avito.ru'
data = []

def random_headers():
    return {'User-Agent': choice(desktop_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}



ro = re.get(URL, headers=random_headers())
print(ro.status_code)
so = BeautifulSoup(ro.text, 'lxml')

pg = so.find('div', class_='pagination-root-Ntd_O').find_all('span', class_='pagination-item-JJq_j')
pn1 = str(pg[7])
print(pn1)
pn2 = pn1[pn1.find('">')+2:pn1.find('</')]
print(pn2)
for p in range(1, int(pn2)+1):
    print(p)
    url = f"https://www.avito.ru/murmanskaya_oblast/kvartiry/prodam-ASgBAgICAUSSA8YQ?cd=1&p={p}"
    r = re.get(url, headers=random_headers())
    print(url)
    sleep(5)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'lxml')
        s = soup.findAll('div', class_='iva-item-root-_lk9K photo-slider-slider-S15A_ iva-item-list-rfgcH '
                                    'iva-item-redesign-rop6P iva-item-responsive-_lbhG iva-item-ratingsRedesign-ydZfp '
                                    'items-item-My3ih items-listItem-Gd1jN js-catalog-item-enum')
        print(len(s))
        for i in s:
            link = host+i.find('a', class_='iva-item-sliderLink-uLz1v').get('href')
            nid = link[link.rfind('_')+1:] # ид записи
            titl = i.find('h3', class_='title-root-zZCwT iva-item-title-py3i_ title-listRedesign-_rejR '
                                       'title-root_maxHeight-X6PsH text-text-LurtD text-size-s-BxGpL '
                                       'text-bold-SinUO').get_text().replace(' ', '').replace('\xa0', '')
            o_txt = i.find('div',
                           class_='iva-item-text-Ge6dR iva-item-description-FDgK4 text-text-LurtD text-size-s-BxGpL'
                        ).get_text()
            # Площадь
            total_area = titl[titl.find(',')+1:titl.find('м²')]
            # этаж
            storeys = titl[titl.find('/')-1:titl.find('/')]
            # Всего этажей
            number_of_storeys = titl[titl.find('/')+1:titl.find('э')]
            town = i.find('div', class_='geo-georeferences-SEtee text-text-LurtD text-size-s-BxGpL').find('span').get_text()
            if i.find('span', class_='geo-address-fhHd0 text-text-LurtD text-size-s-BxGpL').find('span').get_text():
                addr = i.find('span', class_='geo-address-fhHd0 text-text-LurtD text-size-s-BxGpL').find('span').get_text()
            else:
                addr = ''
            print(addr)
            data.append({
                'id': nid,
                'link': link , 'title': titl, 'txt': o_txt,
                'town': town, 'addres': addr, 'total_area': total_area,
                'storeys': storeys, 'number_of_storeys': number_of_storeys
            })
            # pdfF = pdfkit.from_url(link, False)
            # pdfkit.from_url(pdfF, '1.pdf')
print(data)
with open('data.json', 'w') as fout:
    json.dump(data, fout)

