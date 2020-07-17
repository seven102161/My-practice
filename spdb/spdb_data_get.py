import requests
import time
import random
from crawler_tool import CrawlerTool


def main(p_type, start_=1, end_=2):
    global info_list
    global proxy
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
        'Cookie': 'Hm_lvt_e3386c9713baeb4f5230e617a0255dcb=1594953789; Hm_lpvt_e3386c9713baeb4f5230e617a0255dcb=1594965610; TSPD_101=08e305e14cab28004111c979e708c0f58aca3996a5e326992f37a1fa2be3fdaf2fc60b8c64eb62f9877a661438351336:; JSESSIONID=8C2A57A56C5B5F98402AAFBA4A178A01; TS01d02f4c=01ea722d2a88f7179e9a4a43e566099a06e83dcbc7cfed48ee5984a71615e533ed870f770969c0907091ff10a68ebc637f461f1bdb4751205064a52c2e0a6f634c9c91fc20',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.13 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    for i in range(start_, end_):
        pg = str(i)
        product_type = "(pType='{}')".format(p_type)
        data = {
            'metadata': 'pName|pCode|pType|pZpD|pGpS|pPub|pRisk|pPart|pMoney|pStatus|pForm',
            'channelid': '213326',
            'page': pg,
            'searchword': product_type,
        }

        proxies = {
            'http': proxy,
        }
        print(f'get page {pg}, content {p_type}=============================')
        try:
            response = requests.post(url, headers=headers, data=data, proxies=proxies)
            if response.status_code == 200:
                print(response.status_code)
                # print(response.text)
                json_data = response.json()
                info_list.append(json_data)
                time.sleep(10)
            else:
                print(response.status_code)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    pType_list = ['理财', '基金证券', '信托', '保险', '结构性存款', '贵金属商品外汇']
    proxy_list = CrawlerTool.get_proxy()
    proxy = random.choice(proxy_list)
    info_list = []
    main(pType_list[0], 1, 7)
    CrawlerTool.write_to_json('spdb_data_original.json', info_list)
