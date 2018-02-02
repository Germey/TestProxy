import requests
import time
import numpy as np
from requests.exceptions import ProxyError, ConnectTimeout, ReadTimeout, SSLError, ConnectionError
import sys
from pyquery import PyQuery as pq

test_url = 'https://www.baidu.com/'
timeout = 60
count = 500


def test_proxy(proxy):
    try:
        proxies = {
            'https': 'http://' + proxy
        }
        start_time = time.time()
        requests.get(test_url, timeout=timeout, proxies=proxies)
        end_time = time.time()
        used_time = end_time - start_time
        print('Proxy Valid:', proxy, 'Used Time:', used_time)
        return True, used_time
    except (ProxyError, ConnectTimeout, SSLError, ReadTimeout, ConnectionError):
        print('Proxy Invalid:', proxy)
        return False, None


def test_proxies(proxies):
    used_time_list = []
    valid_count = 0
    total_count = len(proxies)
    for index, proxy in enumerate(proxies):
        print('Case', index + 1, 'Testing', proxy)
        flag, result = test_proxy(proxy)
        if flag:
            used_time_list.append(result)
            valid_count += 1
    used_time_array = np.asarray(used_time_list, np.float32)
    print('Used Time Mean:', used_time_array.mean(),
          'Used Time Var', used_time_array.var(),
          'Valid Count:', valid_count,
          'Total Count:', total_count,
          'Valid Percent: %.2f%%' % (valid_count * 100.0 / total_count))


def main():
    proxies = []
    for page in range(1, 30):
        start_url = 'http://www.xicidaili.com/wt/{}'.format(page)
        print(start_url)
        html = requests.get(start_url, headers={
            'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}).text
        doc = pq(html)
        items = list(doc('#ip_list tr').items())
        for item in items[1:]:
            ip = item.find('td:nth-child(2)').text()
            port = item.find('td:nth-child(3)').text()
            proxy = ip.strip() + ':' + port.strip()
            proxies.append(proxy)
            if len(proxies) == count:
                print('Total', len(proxies))
                test_proxies(proxies)
                break


if __name__ == '__main__':
    main()
