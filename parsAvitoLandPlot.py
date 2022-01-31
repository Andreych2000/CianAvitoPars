from random import choice
from random import randint
import requests as re
from bs4 import BeautifulSoup
from time import sleep
import json
# import pdfkit
# import imgkit
from html2image import Html2Image
# from weasyprint import HTML

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

URL = 'https://www.avito.ru/murmanskaya_oblast/zemelnye_uchastki/sdam-ASgBAgICAUSWA9wQ'
HOST = 'https://www.avito.ru'
# PATH_WK = r'/usr/bin/wkhtmltopdf' # Место установки
# CONFIG = imgkit.config(wkhtmltopdf=PATH_WK)
# hti = Html2Image()
hti = Html2Image(output_path='pdf', size=(2500, 3500))
data = []

def random_headers():
    return {'User-Agent': choice(DESKTOP_AGENTS),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}



ro = re.get(URL, headers=random_headers())
print(ro.status_code)
so = BeautifulSoup(ro.text, 'lxml')
# print(so.text)
s = so.find('div', {'data-marker': 'catalog-serp'}).find_all('div', class_='iva-item-root-_lk9K photo-slider-slider-S15A_ '
                                                                      'iva-item-list-rfgcH iva-item-redesign-rop6P '
                                                                      'iva-item-responsive-_lbhG '
                                                                      'iva-item-ratingsRedesign-ydZfp '
                                                                      'items-item-My3ih items-listItem-Gd1jN '
                                                                      'js-catalog-item-enum')
print(len(s))
for i in s:
    sl = randint(1, 5)
    print('Задержка' + ' - ' + str(sl) + ' ' + 'секунд')
    sleep(sl)
    link = HOST + i.find('a', class_='iva-item-sliderLink-uLz1v').get('href')
    print(link)
    sleep(1)
    Sr = re.get(link, allow_redirects=True, headers=random_headers())
    Ssoup = BeautifulSoup(Sr.text, 'lxml')
    total_price = Ssoup.find('div', class_='item-price-wrapper').find('span', class_='js-item-price').get(
        'content')
    print('Цена' + ' ' + total_price)
    addres = Ssoup.find('div', {'itemprop': 'address'}).find('span', class_='item-address__string').get_text().strip()
    print('Адрес'+' '+addres)
    total_area = Ssoup.find('li', class_='item-params-list-item').get_text().strip().replace('Площадь:','')
    print(total_area)
    if i.find('div',
              class_='iva-item-text-Ge6dR iva-item-description-FDgK4 text-text-LurtD text-size-s-BxGpL') == None:
        o_txt_t = ''
    else:
        o_txt_t = i.find('div',
                         class_='iva-item-text-Ge6dR iva-item-description-FDgK4 text-text-LurtD text-size-s-BxGpL'
                         ).get_text()
        xb0 = o_txt_t.replace('\xb2', ' ')
        u20bd = xb0.replace('\u20bd', ' ')
        xa0 = u20bd.replace('\xa0', ' ')
        u2011 = xa0.replace('\u2011', ' ')
        o_txt = u2011.replace('\n', '')
        print(o_txt)



