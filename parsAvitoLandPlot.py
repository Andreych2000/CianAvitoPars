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
URL = 'https://www.avito.ru/murmanskaya_oblast/zemelnye_uchastki'
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

pg = so.find('div', class_='pagination-root-Ntd_O').find_all('span', class_='pagination-item-JJq_j')
pn1 = str(pg[7])
print(pn1)
pn2 = pn1[pn1.find('">')+2:pn1.find('</')]
print(pn2)
# for p in range(1, int(pn2)+1):
for p in range(1, 2):
    print(p)
    url = f"https://www.avito.ru/murmanskaya_oblast/zemelnye_uchastki?p={p}"
    r = re.get(url, headers=random_headers())
    print(url)
    # генерим случайное число
    sl = randint(5, 20)
    print('Задержка'+' - '+str(sl)+' '+'секунд')
    sleep(sl)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'lxml')
        s = soup.findAll('div', class_='iva-item-root-_lk9K photo-slider-slider-S15A_ iva-item-list-rfgcH '
                                       'iva-item-redesign-rop6P iva-item-responsive-_lbhG '
                                       'iva-item-ratingsRedesign-ydZfp items-item-My3ih items-listItem-Gd1jN '
                                       'js-catalog-item-enum')
        print(len(s))
        for i in s:
            sl = randint(1, 5)
            print('Задержка'+' - '+str(sl)+' '+'секунд')
            sleep(sl)
            link = HOST+i.find('a', class_='iva-item-sliderLink-uLz1v').get('href')
            print(link)
            nid = link[link.rfind('_')+1:] # ид записи
            print(nid)
            titl = i.find('h3', class_='title-root-zZCwT iva-item-title-py3i_ title-listRedesign-_rejR '
                                       'title-root_maxHeight-X6PsH text-text-LurtD text-size-s-BxGpL '
                                       'text-bold-SinUO').get_text().replace(' ', ' ').replace('\xa0', ' ')
            if i.find('div', class_='iva-item-text-Ge6dR iva-item-description-FDgK4 text-text-LurtD text-size-s-BxGpL') == None:
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
            sleep(sl)
            Surl = link
            Sr = re.get(Surl, allow_redirects=True, headers=random_headers())
            nameHTML = 'html/' + nid + '.html'
            print(nameHTML)
            with open(nameHTML, 'wb') as file:
                file.write(Sr.content)
                file.close()
            # sleep(1)
            namePNG = 'pdf/'+nid+'.pdf'
            hti.screenshot(other_file=nameHTML, save_as=namePNG)
            # HTML(Surl).write_pdf(namePDF)
            # print(namePDF)
            # pdfkit.from_url(Surl, namePDF, configuration=CONFIG)
            # pdfkit.from_file(nameHTML, namePDF)
            # nameJPG = 'pdf/' + nid + '.jpg'
            # imgkit.from_url(Surl, nameJPG)
            # hti.screenshot(url=Surl, save_as=namePNG)
            Ssoup = BeautifulSoup(Sr.text, 'lxml')
            # Площадь
            # total_area = titl[titl.find(',') + 1:titl.find('м²')]
            # Цена
            total_price = Ssoup.find('div', class_='item-price-wrapper').find('span', class_='js-item-price').get('content')
            print('Цена'+' '+total_price)
            # этаж
            storeys = titl[titl.find('/') - 1:titl.find('/')]
            print(storeys)
            # Всего этажей
            number_of_storeys = titl[titl.find('/') + 1:titl.find('э')]
            print(number_of_storeys)
            # if i.find('div', class_='geo-georeferences-SEtee text-text-LurtD text-size-s-BxGpL') == None:
            #     town = ''
            # else:
            #     town = i.find('div', class_='geo-georeferences-SEtee text-text-LurtD text-size-s-BxGpL').find(
            #         'span').get_text()
            if i.find('span', class_='geo-address-fhHd0 text-text-LurtD text-size-s-BxGpL') == None:
                town = ''
            else:
                town = i.find('span', class_='geo-address-fhHd0 text-text-LurtD text-size-s-BxGpL').find(
                    'span').get_text()
            print(town)
            data.append(dict(id=nid, link=link, title=titl, txt=o_txt, town=town, total_price=total_price,
                             storeys=storeys, number_of_storeys=number_of_storeys))
print(data)
with open('LandPlot.json', 'w') as fout:
    json.dump(data, fout, ensure_ascii=False)