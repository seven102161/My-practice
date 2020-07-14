import requests
import json
import random
import re
import time


def main():
    global proxy_list
    global product_list
    base_url = 'https://www.cmbchina.com/cfweb/svrajax/product.ashx?'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
        'Referer': 'https://www.cmbchina.com/cfweb/CDeposit/Default.aspx',
    }

    for i in range(1, 14):
        params = {
            'op': 'search',
            'type': 'm',
            'pageindex': str(i),
            'series': '06',
            'pagesize': '200',
            'orderby': 'ord1',
            't': '0.5894851352924873',
        }
        proxies = random.choice(proxy_list)
        res = requests.get(base_url, headers=headers, params=params, proxies={'http': proxies})
        if res.status_code == 200:
            print('get page {}'.format(i))
            data = res.text
            # print(data)
            info_c = re.compile(r'(PrdCode:".*?ProxyText:"")', re.S)
            info_r = info_c.findall(data)
            product_list.extend(info_r)
        else:
            print(res.status_code)
        time.sleep(random.randint(2, 5))


def write_to_json(product_list):
    with open('cmb_data_original.json', 'w', encoding='utf-8') as fp:
        json.dump(product_list, fp)
    print('done')


if __name__ == '__main__':
    proxy_data = open('proxy.json').read()
    proxy_list = json.loads(proxy_data)
    product_list = []
    main()
    # print(product_list)
    write_to_json(product_list)
