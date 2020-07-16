import requests
import re
import time
import random
from crawler_tool import CrawlerTool


def main(start_=1, end_=2):
    global info_list
    # global proxy_list
    url = 'https://per.spdb.com.cn/was5/web/search'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Host': 'per.spdb.com.cn',
        'Origin': 'https://per.spdb.com.cn',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
        'Referer': 'https://per.spdb.com.cn/bank_financing/cxpt/?TSPD_101=08e305e14cab28001708bd6fadff00237c46c1757eee754f04284e78610bc42494dffd13aa59f66481c546a5b6452f2c%3a',
        'Content-Length': '130',
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie': 'TS01d02f4c=01ea722d2aecb986ce4c6b7de590514941fdb89e69d77d578c2ab5400620dc56fa7e5d9406a2687454350467198ad348b344d5e504720f082e1a592c80327829c95b6a511f; JSESSIONID=FE31AA4607BA23361199992DD10E2367',
    }
    for i in range(start_, end_):
        pg = str(i)
        params = {
            'metadata': 'pName|pCode|pType|pZpD|pGpS|pPub|pRisk|pPart|pMoney|pStatus|pForm',
            'channelid': '213326',
            'page': pg,
        }
        # proxies = {
        #     'http': random.choice(proxy_list),
        # }
        try:
            # response = requests.post(url, headers=headers, data=data, proxies=proxies)
            response = requests.post(url, headers=headers, params=params)
            original_data = response.text
            data_list = re.findall(r'{"pPub":".*?","pStatus":".*?","pPart":".*?","pName":".*?","pGpS":".*?","pCode":".*?","pZpD":".*?","pMoney":".*?","pRisk":".*?","pType":".*?","pForm":".*?"}', original_data, re.S)
            print(f'page {pg} get, show first line as below:\n', {data_list[0]})
            info_list.append(data_list)
            time.sleep(1)
            response.close()
            time.sleep(random.randint(3, 6))
        except Exception as e:
            print(e)


if __name__ == '__main__':
    # proxy_list = CrawlerTool.get_proxy()
    # print(proxy_list)
    info_list = []
    main()
    # CrawlerTool.write_to_json('spdb_data_original.json', info_list)
