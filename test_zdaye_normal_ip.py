from public import get_page, test_proxy, max, stats_result, is_proxy
import time

api_url = 'http://api.zdaye.com/?api=201802021546098646&rtype=1&ct=1'
wait = 4


def main():
    print('Testing zdaye normal ip')
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
