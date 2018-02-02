import requests
import time
import numpy as np
from requests.exceptions import ProxyError, ConnectTimeout, ReadTimeout, SSLError, ConnectionError
import sys
import io
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
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


def test_my_proxies():
    proxies = []
    print('Getting Proxies')
    for i in range(count):
        response = requests.get('http://azure7.cuiqingcai.com:5555/random')
        proxy = response.text.strip()
        proxies.append(proxy)
        print('Got', i + 1, 'Proxy')
        if len(proxies) == count:
            break
    test_proxies(proxies)

def test_zhandaye_normal_ip():
    proxies = []
    print('Getting Proxies')
    response = requests.get('http://api.zdaye.com/?api=201802021546098646&rtype=1&ct=500')
    proxies = response.text.split('\n')
    print('Got', len(proxies), 'Proxy')
    proxies = list(map(lambda x: x.strip(), proxies))
    test_proxies(proxies)

def test_zhandaye_good_ip():
    used_time_list = []
    valid_count = 0
    proxy_list = []
    for _ in range(100):
        time.sleep(12)
        response = requests.get('http://s.zdaye.com/?api=201802021609421496&count=500&px=2')
        proxies = response.text.split('\n')
        proxies = list(map(lambda x: x.strip(), proxies))
        for index, proxy in enumerate(proxies):
            print('Case', len(proxy_list), 'Testing', proxy)
            flag, result = test_proxy(proxy)
            if flag:
                used_time_list.append(result)
                valid_count += 1
            proxy_list.append(proxy)
            if len(proxy_list) == count:
                total_count = len(proxy_list)
                used_time_array = np.asarray(used_time_list, np.float32)
                print('Used Time Mean:', used_time_array.mean(),
                      'Used Time Var', used_time_array.var(),
                      'Valid Count:', valid_count,
                      'Total Count:', total_count,
                      'Valid Percent: %.2f%%' % (valid_count * 100.0 / count))

def test_abuyun_pro():
    print('Pro')
    targetUrl = "http://test.abuyun.com/proxy.php"
    #targetUrl = "http://proxy.abuyun.com/switch-ip"
    #targetUrl = "http://proxy.abuyun.com/current-ip"

    # 代理服务器
    proxyHost = "http-pro.abuyun.com"
    proxyPort = "9010"

    # 代理隧道验证信息
    proxyUser = "HTS9F6LOP609C29P"
    proxyPass = "9DCF94E75F951713"

    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
      "host" : proxyHost,
      "port" : proxyPort,
      "user" : proxyUser,
      "pass" : proxyPass,
    }

    proxies = {
        "http"  : proxyMeta,
        "https" : proxyMeta,
    }

    used_time_list = []
    valid_count = 0
    total_count = len(proxies)
    for index in range(count):
        time.sleep(1)
        print('Case', index + 1, 'Testing')
        try:
            start_time = time.time()
            requests.get(test_url, timeout=timeout, proxies=proxies)
            end_time = time.time()
            used_time = end_time - start_time
            print('Proxy Valid:', 'Used Time:', used_time)
            used_time_list.append(used_time)
            valid_count += 1
        except (ProxyError, ConnectTimeout, SSLError, ReadTimeout, ConnectionError):
            print('Proxy Invalid:')
    used_time_array = np.asarray(used_time_list, np.float32)
    print('Used Time Mean:', used_time_array.mean(),
          'Used Time Var', used_time_array.var(),
          'Valid Count:', valid_count,
          'Total Count:', total_count,
          'Valid Percent: %.2f%%' % (valid_count * 100.0 / count))


def test_abuyun_dyn():
    print('Dyn')
    targetUrl = "http://test.abuyun.com/proxy.php"
    #targetUrl = "http://proxy.abuyun.com/switch-ip"
    #targetUrl = "http://proxy.abuyun.com/current-ip"

    # 代理服务器
    proxyHost = "http-dyn.abuyun.com"
    proxyPort = "9020"

    # 代理隧道验证信息
    proxyUser = "HZUQP68AU2TM2ZYD"
    proxyPass = "AA000BA6E821EA1C"

    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
      "host" : proxyHost,
      "port" : proxyPort,
      "user" : proxyUser,
      "pass" : proxyPass,
    }

    proxies = {
        "http"  : proxyMeta,
        "https" : proxyMeta,
    }

    used_time_list = []
    valid_count = 0
    total_count = len(proxies)
    for index in range(count):
        time.sleep(1)
        print('Case', index + 1, 'Testing')
        try:
            start_time = time.time()
            requests.get(test_url, timeout=timeout, proxies=proxies)
            end_time = time.time()
            used_time = end_time - start_time
            print('Proxy Valid:', 'Used Time:', used_time)
            used_time_list.append(used_time)
            valid_count += 1
        except (ProxyError, ConnectTimeout, SSLError, ReadTimeout, ConnectionError):
            print('Proxy Invalid:')
    used_time_array = np.asarray(used_time_list, np.float32)
    print('Used Time Mean:', used_time_array.mean(),
          'Used Time Var', used_time_array.var(),
          'Valid Count:', valid_count,
          'Total Count:', total_count,
          'Valid Percent: %.2f%%' % (valid_count * 100.0 / count))


def test_abuyun_cla():
    print('cla')
    targetUrl = "http://test.abuyun.com/proxy.php"
    #targetUrl = "http://proxy.abuyun.com/switch-ip"
    #targetUrl = "http://proxy.abuyun.com/current-ip"

    # 代理服务器
    proxyHost = "http-cla.abuyun.com"
    proxyPort = "9030"

    # 代理隧道验证信息
    proxyUser = "HJ5182561IJ160FC"
    proxyPass = "04CCF0E91519F7A8"

    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
      "host" : proxyHost,
      "port" : proxyPort,
      "user" : proxyUser,
      "pass" : proxyPass,
    }

    proxies = {
        "http"  : proxyMeta,
        "https" : proxyMeta,
    }

    used_time_list = []
    valid_count = 0
    total_count = len(proxies)
    for index in range(count):
        time.sleep(1)
        print('Case', index + 1, 'Testing')
        try:
            start_time = time.time()
            requests.get(test_url, timeout=timeout, proxies=proxies)
            end_time = time.time()
            used_time = end_time - start_time
            print('Proxy Valid:', 'Used Time:', used_time)
            used_time_list.append(used_time)
            valid_count += 1
        except (ProxyError, ConnectTimeout, SSLError, ReadTimeout, ConnectionError):
            print('Proxy Invalid:')
    used_time_array = np.asarray(used_time_list, np.float32)
    print('Used Time Mean:', used_time_array.mean(),
          'Used Time Var', used_time_array.var(),
          'Valid Count:', valid_count,
          'Total Count:', total_count,
          'Valid Percent: %.2f%%' % (valid_count * 100.0 / count))


def test_mogu_baoliang():
    print('mogubaoliang')
    used_time_list = []
    valid_count = 0
    proxy_list = []
    for _ in range(100):
        response = requests.get('http://piping.mogumiao.com/proxy/api/get_ip_al?appKey=03aaeef6cf0e41289cb54e630c605847&count=20&expiryDate=0&format=2')
        proxies = response.text.split('\n')
        proxies = list(map(lambda x: x.strip(), proxies))
        for index, proxy in enumerate(proxies):
            if proxy:
                print('Case', len(proxy_list), 'Testing', proxy)
                flag, result = test_proxy(proxy)
                if flag:
                    used_time_list.append(result)
                    valid_count += 1
                proxy_list.append(proxy)
                if len(proxy_list) == count:
                    total_count = len(proxy_list)
                    used_time_array = np.asarray(used_time_list, np.float32)
                    print('Used Time Mean:', used_time_array.mean(),
                          'Used Time Var', used_time_array.var(),
                          'Valid Count:', valid_count,
                          'Total Count:', total_count,
                          'Valid Percent: %.2f%%' % (valid_count * 100.0 / total_count))



def test_mogu_baoshi():
    print('mogubaoshi')
    used_time_list = []
    valid_count = 0
    proxy_list = []
    for _ in range(100):
        response = requests.get('http://piping.mogumiao.com/proxy/api/get_ip_bs?appKey=d3ddf6513bc84652a99b32f06d5b6027&count=20&expiryDate=0&format=2')
        proxies = response.text.split('\n')
        proxies = list(map(lambda x: x.strip(), proxies))
        for index, proxy in enumerate(proxies):
            if proxy:
                try:
                    print('Case', len(proxy_list), 'Testing', proxy)
                except UnicodeEncodeError:
                    continue
                flag, result = test_proxy(proxy)
                if flag:
                    used_time_list.append(result)
                    valid_count += 1
                proxy_list.append(proxy)
                if len(proxy_list) == count:
                    total_count = len(proxy_list)
                    used_time_array = np.asarray(used_time_list, np.float32)
                    print('Used Time Mean:', used_time_array.mean(),
                          'Used Time Var', used_time_array.var(),
                          'Valid Count:', valid_count,
                          'Total Count:', total_count,
                          'Valid Percent: %.2f%%' % (valid_count * 100.0 / total_count))
from pyquery import PyQuery as pq
def crawl_xicidaili():
    proxies = []
    import re
    for page in range(1, 30):
        start_url = 'http://www.xicidaili.com/wt/{}'.format(page)
        print(start_url)
        html = requests.get(start_url, headers={'User-Agent':'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}).text
        #print(html)
        #ip_adress = re.compile('<td class="country"><img src="http://fs.xicidaili.com/images/flag/cn.png" alt="Cn" /></td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>', re.S)
        #ip_adress = re.compile('<td class="country"><img src="http://fs.xicidaili.com/images/flag/cn.png" alt="Cn" /></td>\s*<td>(.*?)</td>\s*<td>(.*?)</td>')
        doc = pq(html)
        items = list(doc('#ip_list tr').items())
        for item in items[1:]:
            ip = item.find('td:nth-child(2)').text()
            port = item.find('td:nth-child(3)').text()
            #print(ip, port)
        # \s* 匹配空格，起到换行作用
            proxy = ip.strip()+':'+port.strip()
            proxies.append(proxy)
            if len(proxies) == count:
                print('Total', len(proxies))
                test_proxies(proxies)
                break

def test_daxiang():
    print('Daxiang')
    proxies = []
    print('Getting Proxies')
    response = requests.get('http://tvp.daxiangdaili.com/ip/?tid=559363191592228&num=500')
    proxies = response.text.split('\n')
    print('Got', len(proxies), 'Proxy')
    proxies = list(map(lambda x: x.strip(), proxies))
    test_proxies(proxies)

def test_quanwangdaili_free():
    print('quanwangdailifree')
    proxies = []
    import re
    for i in range(200):
        start_url = 'http://www.goubanjia.com/free/gngn/index{i}.shtml'.format(i=i)
        html = requests.get(start_url,headers={'User-Agent':'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}).text
        print(start_url)
        #print(html)
        if html:
            print('htmlok')
            doc = pq(html)
            tds = doc('td.ip').items()
            for td in tds:
                #print(td)
                td.find('p').remove()
                proxy =  td.text().replace(' ', '')
                proxies.append(proxy)
                if len(proxies) == count:
                    print('Total', len(proxies))
                    test_proxies(proxies)
                    break
            print(len(proxies))

def test_quwangdailiputong():
    print('quanwangputong')
    proxies = []
    print('Getting Proxies')
    response = requests.get('http://api.goubanjia.com/api/get.shtml?order=8e1741e69f65fdbe56a0713eff1e54fb&num=500&carrier=0&protocol=0&an1=1&an2=2&an3=3&sp1=1&sp2=2&sp3=3&sort=1&system=1&distinct=0&rettype=1&seprator=%0A')
    proxies = response.text.split('\n')
    proxies = proxies[0:500]
    print('Got', len(proxies), 'Proxy')
    proxies = list(map(lambda x: x.strip(), proxies))
    test_proxies(proxies)


def test_quwangdailidongtai():
    print('quanwangdongtai')
    proxies = []
    valid_count = 0
    times = []
    print('Getting Proxies')
    for i in range(600):
        time.sleep(5)
        try:
            response = requests.get('http://dynamic.goubanjia.com/dynamic/get/8e1741e69f65fdbe56a0713eff1e54fb.html')
            proxy = response.text.strip()
            flag, result = test_proxy(proxy)
            if flag:
                valid_count +=1
                times.append(result)
            proxies.append(proxy)
            print(proxy)
            if len(proxies) == count:
                used_time_array = np.asarray(times, np.float32)
                print('Used Time Mean:', used_time_array.mean(),
                      'Used Time Var', used_time_array.var(),
                      'Valid Count:', valid_count,
                      'Total Count:', count,
                      'Valid Percent: %.2f%%' % (valid_count * 100.0 / count))
        except:
            pass




def test_yundaili():
    print('yundaili')
    data = [
        ('key', '20180202220426620'),
        ('getnum', '500'),
        ('isp', '0'),
        ('anonymoustype', '0'),
        ('start', ''),
        ('port', ''),
        ('notport', ''),
        ('ipaddress', ''),
        ('unaddress', ''),
        ('area', '0'),
        ('formats', '1'),
        ('splits', ''),
        ('proxytype', '0'),
        ('proxytype', '1'),
        ('proxytype', '2'),
        ('proxytype', '3'),
        ('ports', ''),
        ('ports', '8087'),
        ('ports', '24852'),
        ('ports', '48376'),
        ('ports', '6080'),
        ('ports', '42565'),
        ('ports', '49063'),
        ('ports', '42419'),
        ('ports', '9000'),
        ('ports', '63000'),
        ('ports', '21114'),
        ('ports', '36846'),
        ('ports', '8118'),
        ('ports', '61234'),
        ('ports', '31281'),
        ('ports', '21320'),
        ('ports', '64672'),
        ('ports', '53282'),
        ('ports', '45619'),
        ('ports', '8090'),
        ('ports', '8980'),
        ('ports', '50809'),
        ('ports', '9999'),
        ('ports', '888'),
        ('ports', '61872'),
        ('ports', '48877'),
        ('ports', '8181'),
        ('ports', '1234'),
        ('ports', '42233'),
        ('ports', '8081'),
        ('ports', '55555'),
        ('ports', '54132'),
        ('ports', '37816'),
        ('ports', '8585'),
        ('ports', '3129'),
        ('ports', '8888'),
        ('ports', '39325'),
        ('ports', '44311'),
        ('ports', '1337'),
        ('ports', '6006'),
        ('ports', '8213'),
        ('ports', '53806'),
        ('ports', '53005'),
        ('ports', '61587'),
        ('ports', '49201'),
        ('ports', '48173'),
        ('ports', '37814'),
        ('ports', '39829'),
        ('ports', '81'),
        ('ports', '35564'),
        ('ports', '45543'),
        ('ports', '29075'),
        ('ports', '8800'),
        ('ports', '18192'),
        ('ports', '30094'),
        ('ports', '62225'),
        ('ports', '8328'),
        ('ports', '48285'),
        ('ports', '8082'),
        ('ports', '40691'),
        ('ports', '3127'),
        ('ports', '1080'),
        ('ports', '808'),
        ('ports', '3130'),
        ('ports', '10200'),
        ('ports', '62637'),
        ('ports', '65205'),
        ('ports', '34803'),
        ('ports', '87'),
        ('ports', '32473'),
        ('ports', '30054'),
        ('ports', '54846'),
        ('ports', '7667'),
        ('ports', '36832'),
        ('ports', '8099'),
        ('ports', '90'),
        ('ports', '31288'),
        ('ports', '54214'),
        ('ports', '54924'),
        ('ports', '54314'),
        ('ports', '2000'),
        ('ports', '63909'),
        ('ports', '30613'),
        ('ports', '15963'),
        ('ports', '8091'),
        ('ports', '8878'),
        ('ports', '8383'),
        ('ports', '24487'),
        ('ports', '22000'),
        ('ports', '37918'),
        ('ports', '42071'),
        ('ports', '25778'),
        ('ports', '35548'),
        ('ports', '27421'),
        ('ports', '1997'),
        ('ports', '8380'),
        ('ports', '62386'),
        ('ports', '24868'),
        ('ports', '4444'),
        ('ports', '64444'),
        ('ports', '88'),
        ('ports', '49817'),
        ('ports', '40245'),
        ('ports', '8085'),
        ('ports', '9797'),
        ('ports', '39704'),
        ('ports', '40391'),
        ('ports', '62000'),
        ('ports', '10000'),
        ('ports', '8128'),
        ('ports', '9090'),
        ('ports', '28274'),
        ('ports', '42340'),
        ('ports', '39647'),
        ('ports', '2020'),
        ('ports', '1081'),
        ('ports', '8088'),
        ('ports', '6660'),
        ('ports', '22063'),
        ('ports', '54566'),
        ('ports', '82'),
        ('ports', '8197'),
        ('ports', '48678'),
        ('ports', '31417'),
        ('ports', '51552'),
        ('ports', '65103'),
        ('ports', '53281'),
        ('ports', '8083'),
        ('ports', '3128'),
        ('ports', '42619'),
        ('ports', '47482'),
        ('ports', '52225'),
        ('ports', '1920'),
        ('ports', '27788'),
        ('ports', '21886'),
        ('ports', '8086'),
        ('ports', '58391'),
        ('ports', '8000'),
        ('ports', '80'),
        ('ports', '52311'),
        ('ports', '39275'),
        ('ports', '51816'),
        ('ports', '6666'),
        ('ports', '555'),
        ('ports', '49921'),
        ('ports', '23618'),
        ('ports', '46248'),
        ('ports', '42421'),
        ('ports', '57624'),
        ('ports', '8089'),
        ('ports', '41239'),
        ('ports', '83'),
        ('ports', '49695'),
        ('ports', '65301'),
        ('ports', '3137'),
        ('ports', '15600'),
        ('ports', '65309'),
        ('ports', '7777'),
        ('ports', '30528'),
        ('ports', '20535'),
        ('ports', '52305'),
        ('ports', '21468'),
        ('ports', '8123'),
        ('ports', '18680'),
        ('ports', '8080'),
        ('ports', '8103'),
        ('ports', '52136'),
        ('ports', '443'),
    ]
    print(data)
    response = requests.get(
        'http://www.ip3366.net/action/', data=data)
    proxies = response.text.split('\n')
    proxies = proxies[0:500]
    print('Got', len(proxies), 'Proxy')
    proxies = list(map(lambda x: x.strip(), proxies))
    test_proxies(proxies)

def test_xundaili():
    print('Xundaili')
    used_time_list = []
    valid_count = 0
    proxy_list = []
    for _ in range(100):
        time.sleep(12)
        response = requests.get('http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=da289b78fec24f19b392e04106253f2a&orderno=YZ2018223246g0SAwH&returnType=1&count=10')
        proxies = response.text.split('\n')
        proxies = list(map(lambda x: x.strip(), proxies))
        proxies = list(filter(lambda x: x, proxies))
        for index, proxy in enumerate(proxies):
            print('Case', len(proxy_list), 'Testing', proxy)
            flag, result = test_proxy(proxy)
            if flag:
                used_time_list.append(result)
                valid_count += 1
            proxy_list.append(proxy)
            if len(proxy_list) == count:
                total_count = len(proxy_list)
                used_time_array = np.asarray(used_time_list, np.float32)
                print('Used Time Mean:', used_time_array.mean(),
                      'Used Time Var', used_time_array.var(),
                      'Valid Count:', valid_count,
                      'Total Count:', total_count,
                      'Valid Percent: %.2f%%' % (valid_count * 100.0 / count))


def test_xundaili_duxiang():
    print('Xundaili_duxiang')
    used_time_list = []
    valid_count = 0
    proxy_list = []
    for _ in range(100):
        time.sleep(15)
        response = requests.get('http://api.xdaili.cn/xdaili-api//privateProxy/getDynamicIP/DD2018229551Hn1VYR/c71930d37db611e7bcaf7cd30abda612?returnType=1')
        proxies = response.text.split('\n')
        proxies = list(map(lambda x: x.strip(), proxies))
        proxies = list(filter(lambda x: x, proxies))
        for index, proxy in enumerate(proxies):
            try:
                print('Case', len(proxy_list), 'Testing', proxy)
            except UnicodeEncodeError:
                print('Tel Error')
                continue
            flag, result = test_proxy(proxy)
            if flag:
                used_time_list.append(result)
                valid_count += 1
            proxy_list.append(proxy)
            if len(proxy_list) == count:
                total_count = len(proxy_list)
                used_time_array = np.asarray(used_time_list, np.float32)
                print('Used Time Mean:', used_time_array.mean(),
                      'Used Time Var', used_time_array.var(),
                      'Valid Count:', valid_count,
                      'Total Count:', total_count,
                      'Valid Percent: %.2f%%' % (valid_count * 100.0 / count))


def test_zhima():
    print('zhima')
    used_time_list = []
    valid_count = 0
    proxy_list = []
    for _ in range(100):
        time.sleep(2)
        response = requests.get('http://webapi.http.zhimacangku.com/getip?num=2&type=1&pro=&city=0&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=4&sb=0&pb=4&mr=1&regions=')
        proxies = response.text.split('\n')
        proxies = list(map(lambda x: x.strip(), proxies))
        proxies = list(filter(lambda x: x, proxies))
        for index, proxy in enumerate(proxies):
            try:
                print('Case', len(proxy_list), 'Testing', proxy)
            except UnicodeEncodeError:
                print('Tel Error')
                continue
            flag, result = test_proxy(proxy)
            if flag:
                used_time_list.append(result)
                valid_count += 1
            proxy_list.append(proxy)
            if len(proxy_list) == count:
                total_count = len(proxy_list)
                used_time_array = np.asarray(used_time_list, np.float32)
                print('Used Time Mean:', used_time_array.mean(),
                      'Used Time Var', used_time_array.var(),
                      'Valid Count:', valid_count,
                      'Total Count:', total_count,
                      'Valid Percent: %.2f%%' % (valid_count * 100.0 / count))


def test_taiyang():
    print('taiyang')
    used_time_list = []
    valid_count = 0
    proxy_list = []
    for _ in range(100):
        time.sleep(2)
        response = requests.get('http://http-api.taiyangruanjian.com/getip?num=2&type=1&pro=&city=0&yys=0&port=1&pack=3302&ts=0&ys=0&cs=0&lb=4&sb=0&pb=4&mr=1&regions=')
        proxies = response.text.split('\n')
        proxies = list(map(lambda x: x.strip(), proxies))
        proxies = list(filter(lambda x: x, proxies))
        for index, proxy in enumerate(proxies):
            try:
                print('Case', len(proxy_list), 'Testing', proxy)
            except UnicodeEncodeError:
                print('Tel Error')
                continue
            flag, result = test_proxy(proxy)
            if flag:
                used_time_list.append(result)
                valid_count += 1
            proxy_list.append(proxy)
            if len(proxy_list) == count:
                total_count = len(proxy_list)
                used_time_array = np.asarray(used_time_list, np.float32)
                print('Used Time Mean:', used_time_array.mean(),
                      'Used Time Var', used_time_array.var(),
                      'Valid Count:', valid_count,
                      'Total Count:', total_count,
                      'Valid Percent: %.2f%%' % (valid_count * 100.0 / count))





if __name__ == '__main__':
    test_zhima()
