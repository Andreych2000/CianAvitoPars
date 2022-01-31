import requests as re
from bs4 import BeautifulSoup
# import webbrowser as wb
#
Slink = 'https://www.avito.ru/apatity/kvartiry/2-k._kvartira_43m_45et._2263709222'
# wb.open_new(Slink)
# from html2image import Html2Image
# hti = Html2Image(output_path='pdf', size=(2500, 3500))
# hti.screenshot(other_file='html/2318512606.html', save_as='2318512606.png')

ro = re.get(Slink)
print(ro.status_code)
so = BeautifulSoup(ro.text, 'lxml')
# print(so.contents)
total_price = so.find('div', class_='item-price-wrapper').find('span', class_='js-item-price').get(
                'content')
print('Цена' + ' ' + total_price)
ggg = so.find('ul', class_='item-params-list')
print(ggg)