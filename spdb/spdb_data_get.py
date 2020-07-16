import requests
import re
import time
import random
from crawler_tool import CrawlerTool


def main(min_, max_):
    global info_list
    global proxy_list
    url = 'https://per.spdb.com.cn/was5/web/search'
    headers = {
        'Cookie': 'Hm_lvt_e3386c9713baeb4f5230e617a0255dcb=1594876094,1594876178; Hm_lpvt_e3386c9713baeb4f5230e617a0255dcb=1594876178; TSPD_101=08e305e14cab2800e1bc8af2866b369cd827d13c49865a99f5e3f67446a77a4bceb429f586a49cf3552e61ca7663e766:; JSESSIONID=6863EF990389664754CC7DEF1064B09F; TS01d02f4c=01ea722d2a0ac88b72233a68fdb30bf70b4ef6c395e1e6b274cafb88e3a66c45a1988e4b03b6e455c72a5bca8c1a350ea86bbbc548c6772b1ef4dca710dac5355333aa93f4',
        'Host': 'per.spdb.com.cn',
        'Origin': 'https://per.spdb.com.cn',
        'Referer': 'https://per.spdb.com.cn/bank_financing/cxpt/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.13 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    for i in range(min_, max_):
        pg = str(i)
        params = {
            'metadata': 'pName|pCode|pType|pZpD|pGpS|pPub|pRisk|pPart|pMoney|pStatus|pForm',
            'channelid': '213326',
            'page': pg,
        }
        proxies = random.choice(proxy_list)
        try:
            response = requests.post(url, headers=headers, params=params, proxies={'http': proxies})
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
    proxy_list = CrawlerTool.get_proxy(1)
    print(proxy_list)
    info_list = []
    main(1, 119)
    CrawlerTool.write_to_json('spdb_data_original.json', info_list)
