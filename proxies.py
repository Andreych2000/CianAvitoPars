from proxybroker import Broker
import asyncio
#####################################################################
async def save(proxies, filename):
    with open(filename, 'w') as f:
        while True:
            proxy = await proxies.get()
            if proxy is None:
                break
            row = f'{proxy.host}:{proxy.port}\n'
            f.write(row)


def get_proxies(limit=100):
    proxies = asyncio.Queue()
    broker = Broker(proxies)
    tasks = asyncio.gather(broker.grab(limit=limit),
                           save(proxies, filename='proxies.csv'))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(tasks)
#####################################################################