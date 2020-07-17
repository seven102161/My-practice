import requests
import re
import time
import random
from crawler_tool import CrawlerTool


def get_session():
    web_url = 'https://per.spdb.com.cn/bank_financing/cxpt/'
    session = requests.session()
    session.get(web_url, headers=headers)
    return session


def main(page):
    data_url = 'https://per.spdb.com.cn/was5/web/search'
    data = {
            'metadata': 'pName|pCode|pType|pZpD|pGpS|pPub|pRisk|pPart|pMoney|pStatus|pForm',
            'channelid': '213326',
            'page': str(page),
            'searchword': "(pType='理财')",
        }
    session = get_session()
    response = session.post(data_url, data=data)
    print(response.text)


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.13 Safari/537.36',
    }
    main(1)
