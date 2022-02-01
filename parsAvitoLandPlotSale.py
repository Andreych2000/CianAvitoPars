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

URL = 'https://www.avito.ru/murmanskaya_oblast/zemelnye_uchastki/prodam-ASgBAgICAUSWA9oQ'
HOST = 'https://www.avito.ru'
# PATH_WK = r'/usr/bin/wkhtmltopdf' # Место установки
# CONFIG = imgkit.config(wkhtmltopdf=PATH_WK)
# hti = Html2Image()
hti = Html2Image(output_path='png', size=(2500, 3500))
data = []

def random_headers():
    return {'User-Agent': choice(DESKTOP_AGENTS),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}


###########
ro = re.get(URL, headers=random_headers())
print(ro.status_code)
so = BeautifulSoup(ro.text, 'lxml')
# print(so.text)
pg = so.find('div', class_='pagination-root-Ntd_O').find_all('span', class_='pagination-item-JJq_j')
pn1 = str(pg[7])
print(pn1)
pn2 = pn1[pn1.find('">')+2:pn1.find('</')]
print('Страниц :'+pn2)
for p in range(1, int(pn2)+1):
# for p in range(1, 2):
    print(p)
    url = f"https://www.avito.ru/murmanskaya_oblast/zemelnye_uchastki/prodam-ASgBAgICAUSWA9oQ?p={p}"
    r = re.get(url, headers=random_headers())
    print(url)
    # генерим случайное число
    sl = randint(5, 20)
    print('Задержка' + ' - ' + str(sl) + ' ' + 'секунд')
    sleep(sl)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'lxml')
        s = soup.find('div', {'data-marker': 'catalog-serp'}).find_all('div', class_='iva-item-root-_lk9K '
                                                                                     'photo-slider-slider-S15A_ '
                                                                                     'iva-item-list-rfgcH '
                                                                                     'iva-item-redesign-rop6P '
                                                                                     'iva-item-responsive-_lbhG '
                                                                                     'iva-item-ratingsRedesign-ydZfp '
                                                                                     'items-item-My3ih '
                                                                                     'items-listItem-Gd1jN '
                                                                                     'js-catalog-item-enum')
        print('Объектов :'+' '+ str(len(s)))
        if s != 0:
            for i in s:
                sl = randint(1, 5)
                print('Задержка' + ' - ' + str(sl) + ' ' + 'секунд')
                sleep(sl)
                fileName = i.find('a', class_='iva-item-sliderLink-uLz1v').get('href')
                link = HOST + fileName
                print(link)
                sleep(1)
                Sr = re.get(link, allow_redirects=True, headers=random_headers())
                Ssoup = BeautifulSoup(Sr.text, 'lxml')
                nid = link[link.rfind('_')+1:] # ид записи
                print(nid)
                nameHTML = 'html/' + nid + '.html'
                print(nameHTML)
                with open(nameHTML, 'wb') as file:
                    file.write(Sr.content)
                    file.close()
                namePNG = nid + '.png'
                hti.screenshot(other_file=nameHTML, save_as=namePNG)
                if i.find('h3', class_='title-root-zZCwT iva-item-title-py3i_ title-listRedesign-_rejR '
                                           'title-root_maxHeight-X6PsH text-text-LurtD text-size-s-BxGpL '
                                           'text-bold-SinUO') is None:
                    titl = ''
                else:
                    titl = i.find('h3', class_='title-root-zZCwT iva-item-title-py3i_ title-listRedesign-_rejR '
                                               'title-root_maxHeight-X6PsH text-text-LurtD text-size-s-BxGpL '
                                               'text-bold-SinUO').get_text().replace(' ', ' ').replace('\xa0', ' ')
                print(titl)
                if Ssoup.find('div', class_='item-price-wrapper').find('span', class_='js-item-price') is None:
                    total_price = ''
                else:
                    total_price = Ssoup.find('div',
                                             class_='item-price-wrapper').find('span',
                                                                               class_='js-item-price').get('content')
                print('Цена' + ' ' + total_price)
                if Ssoup.find('div', {'itemprop': 'address'}).find('span', class_='item-address__string') is None:
                    addr = ''
                else:
                    addr = Ssoup.find('div', {'itemprop': 'address'}).find('span',
                                                                           class_='item-address__string').get_text(

                    ).strip()
                print('Адрес'+' '+addr)
                if Ssoup.find('li', class_='item-params-list-item') is None:
                    total_area = ''
                else:
                    total_area = Ssoup.find('li',
                                            class_='item-params-list-item').get_text().strip().replace('Площадь:', '')
                print(total_area)
                if i.find('div', class_='iva-item-text-Ge6dR iva-item-description-FDgK4 text-text-LurtD '
                                        'text-size-s-BxGpL') is None:
                 o_txt_t = ''
                else:
                    o_txt_t = i.find('div', class_='iva-item-text-Ge6dR iva-item-description-FDgK4 text-text-LurtD '
                                                   'text-size-s-BxGpL').get_text()
                    xb0 = o_txt_t.replace('\xb2', ' ')
                    u20bd = xb0.replace('\u20bd', ' ')
                    xa0 = u20bd.replace('\xa0', ' ')
                    u2011 = xa0.replace('\u2011', ' ')
                    o_txt = u2011.replace('\n', '')
                    print(o_txt)
                    object_type = 0
                    data.append(dict(ADDRESS_CITY='', ADDRESS_FULL=addr, DESCRIPTION=o_txt, OBJECT_FLOUR='',
                                     OBJECT_FLOUR_COUNT='', OBJECT_SQUARE=total_area,
                                     OBJECT_TYPE=object_type,
                                     OFFER_COPY_FILENAME=fileName, OFFER_TYPE='продажа', SITE_SOURCE='Авито',
                                     TITLE=titl, PRICE=total_price, URL=link, UUID=nid))
        else:
            print('Объектов нет')
print(data)
with open('avito.LandPlotSale.json', 'w') as fout:
    json.dump(data, fout, ensure_ascii=False)



