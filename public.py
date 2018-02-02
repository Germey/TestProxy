import requests
import time
import numpy as np
from requests.exceptions import ProxyError, ConnectTimeout, ReadTimeout, SSLError, ConnectionError
import re

test_url = 'https://www.baidu.com/'
timeout = 60
max = 500


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


def is_proxy(proxy):
    if re.match('\d+\.\d+\.\d+\.\d+\:\d+', proxy):
        return True
    return False


def test_proxy(proxy=None, proxies=None):
    try:
        if not proxies:
            proxies = {
                'https': 'http://' + proxy
            }
        start_time = time.time()
        requests.get(test_url, timeout=timeout, proxies=proxies)
        end_time = time.time()
        used_time = end_time - start_time
        print('Proxy Valid', 'Used Time:', used_time)
        return True, used_time
    except (ProxyError, ConnectTimeout, SSLError, ReadTimeout, ConnectionError):
        print('Proxy Invalid:', proxy)
        return False, None


def stats_result(used_time_list, valid_count, total_count):
    if not used_time_list or not total_count:
        return
    used_time_array = np.asarray(used_time_list, np.float32)
    print('Total Count:', total_count,
          'Valid Count:', valid_count,
          'Valid Percent: %.2f%%' % (valid_count * 100.0 / total_count),
          'Used Time Mean:', used_time_array.mean(),
          'Used Time Var', used_time_array.var())
