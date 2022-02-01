import requests
import random
from bs4 import BeautifulSoup as bs

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


def get_free_proxies():
    url = "https://free-proxy-list.net/"
    # посылаем HTTP запрос и создаем soup объект
    soup = bs(requests.get(url).content, "html.parser")
    proxies = []
    for row in soup.find("table", class_='table table-striped table-bordered').find_all("tr")[1:]:
        tds = row.find_all("td")
        try:
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            host = f"{ip}:{port}"
            proxies.append(host)
        except IndexError:
            continue
    return proxies
print(get_free_proxies())

def get_session(proxies):
    # создаем сессию для отправки HTTP запроса
    session = requests.Session()
    # выбираем случайным образом один из адресов
    proxy = random.choice(proxies)
    session.proxies = {"http": proxy, "https": proxy}
    return session

for i in range(10):
    s = get_session(get_free_proxies())
    # a = s.get("https://www.avito.ru/murmanskaya_oblast/doma_dachi_kottedzhi", timeout=1.5).text.strip()
    # print(a)
    try:
        print(s.get("https://www.avito.ru/murmanskaya_oblast/doma_dachi_kottedzhi", timeout=1.5).text.strip())
    except Exception as e:
        continue