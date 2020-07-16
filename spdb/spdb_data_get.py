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
        'Accept': 'application/json,text/javascript,*/*; q=0.01',
        'Accept-Encoding': 'gzip,deflate,br',
        'Host': 'per.spdb.com.cn',
        'Origin': 'https://per.spdb.com.cn',
        'Referer': 'https://per.spdb.com.cn/bank_financing/cxpt/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Content-Length': '130',
        'Cookie': 'Hm_lvt_e3386c9713baeb4f5230e617a0255dcb=1594911406; Hm_lpvt_e3386c9713baeb4f5230e617a0255dcb=1594913623; TSPD_101=08e305e14cab280028bae835ca7f8929000c47b90754572eaaf00fec4d6a78fd5c4ac36b0a068730230987d4eb69e84f:; JSESSIONID=2C2C1656A449CC05429F31835775724F; TS01d02f4c=01ea722d2a7cb3a8961af4de85eee1a2b5ae45e4dc308c282010d62676e18208437cedd97a997007e00544cc28a4a97f9f24a7f68b7c5fbb81b47fa4c384a7ca97fced1246',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    for i in range(start_, end_):
        pg = str(i)
        data = {
            'metadata': 'pName|pCode|pType|pZpD|pGpS|pPub|pRisk|pPart|pMoney|pStatus|pForm',
            'channelid': '213326',
            'page': pg,
            'searchword': "(pType='基金证券')",
        }
        # proxies = {
        #     'http': random.choice(proxy_list),
        # }
        try:
            # response = requests.post(url, headers=headers, data=data, proxies=proxies)
            response = requests.post(url, headers=headers, data=data)
            # print(response.status_code)
            if response.status_code == 200:
                original_data = response.text
                data_list = re.findall(r'{"pPub":".*?","pStatus":".*?","pPart":".*?","pName":".*?","pGpS":".*?","pCode":".*?","pZpD":".*?","pMoney":".*?","pRisk":".*?","pType":".*?","pForm":".*?"}', original_data, re.S)
                print(f'page {pg} get, show first line as below:\n', {data_list[0]})
                info_list.append(data_list)
                time.sleep(1)
                response.close()
                time.sleep(random.randint(3, 6))
            else:
                print(response.status_code)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    # proxy_list = CrawlerTool.get_proxy()
    # print(len(proxy_list))
    info_list = []
    main()
    # CrawlerTool.write_to_json('spdb_data_original.json', info_list)
