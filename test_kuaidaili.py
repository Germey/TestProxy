from public import get_page, test_proxy, max, stats_result, is_proxy
import time

api_url = 'http://dev.kuaidaili.com/api/getproxy/?orderid=911759778103322&num=1&b_pcchrome=1&b_pcie=1&b_pcff=1&protocol=1&method=2&an_an=1&an_ha=1&sep=2'
wait = 6


def main():
    print('Testing kuaidaili')
    used_time_list = []
    valid_count = 0
    total_count = 0
    while True:
        flag, result = get_page(api_url)
        if flag:
            proxy = result.strip()
            if is_proxy(proxy):
                total_count += 1
                print('Testing proxy', proxy)
                test_flag, test_result = test_proxy(proxy=proxy)
                if test_flag:
                    valid_count += 1
                    used_time_list.append(test_result)
                stats_result(used_time_list, valid_count, total_count)
        time.sleep(wait)
        if total_count == max:
            break


if __name__ == '__main__':
    main()
