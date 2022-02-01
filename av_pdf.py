# import sys
# from PyQt4.QtCore import *
# import pdfkit
# import imgkit
from weasyprint import HTML
# path_wk = r'/usr/local/bin/wkhtmltopdf' # Место установки
# config = pdfkit.configuration(wkhtmltopdf=path_wk)
# pdfkit.from_url('https://www.avito.ru/murmansk/zemelnye_uchastki/uchastok_15_sot._izhs_1897057262',
#                 'pdf/1897057262.pdf', configuration=config)
# pdfkit.from_url('https://www.avito.ru/molochnyy/zemelnye_uchastki/uchastok_13_sot._snt_dnp_2148819020',
#                 'pdf/2148819020.pdf', configuration=config)
# pdfkit.from_file('1760542867.html', '1760542867.pdf', configuration=config)
# imgkit.from_url('https://www.avito.ru/murmansk/zemelnye_uchastki/uchastok_15_sot._izhs_1897057262',
#                 'pdf/1897057262.jpg')
HTML('https://www.avito.ru/murmansk/zemelnye_uchastki/uchastok_15_sot._izhs_1897057262').write_pdf('pdf/1897057262.pdf')