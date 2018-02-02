import requests
import time
import numpy as np
from requests.exceptions import ProxyError, ConnectTimeout, ReadTimeout, SSLError, ConnectionError

test_url = 'https://www.baidu.com/'
timeout = 60
count = 500


def get_page(url):
    try:
        headers = {
            'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return True, response.text
    except ConnectionError:
        return False, None


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


def stats_result(used_time_list, valid_count, total_count):
    used_time_array = np.asarray(used_time_list, np.float32)
    print('Used Time Mean:', used_time_array.mean(),
          'Used Time Var', used_time_array.var(),
          'Valid Count:', valid_count,
          'Total Count:', total_count,
          'Valid Percent: %.2f%%' % (valid_count * 100.0 / total_count))
