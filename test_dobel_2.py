from public import get_page, test_proxy, max, stats_result, is_proxy
import time

wait = 3

proxy_host = 'http-proxy-sg1.dobel.cn'
proxy_port = '9180'

proxy_user = 'CEPINGHTTTEST2'
proxy_pass = 's6gUwK97'

proxy_meta = 'http://%(user)s:%(pass)s@%(host)s:%(port)s' % {
    'host': proxy_host,
    'port': proxy_port,
    'user': proxy_user,
    'pass': proxy_pass,
}

proxies = {
    'http': proxy_meta,
    'https': proxy_meta,
}


def main():
    print('Testing dobel 2')
    used_time_list = []
    valid_count = 0
    total_count = 0
    while True:
        total_count += 1
        test_flag, test_result = test_proxy(proxies=proxies)
        if test_flag:
            valid_count += 1
            used_time_list.append(test_result)
        stats_result(used_time_list, valid_count, total_count)
        time.sleep(wait)
        if total_count == max:
            break


if __name__ == '__main__':
    main()
