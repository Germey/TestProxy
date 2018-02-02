import requests
from public import get_page

api_url = 'http://api.zdaye.com/?api=201802021546098646&rtype=1&ct=1'


def main():
    print('Getting Proxies')
    used_time_list = []
    while True:
        flag, result = get_page(api_url)
        if flag:
            proxy = result
            

if __name__ == '__main__':
    main()