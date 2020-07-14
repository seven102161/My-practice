import os
import selenium
from selenium import webdriver
import time
from lxml import etree
from excle_wirte import ExcelUtils
import random


class CmbProduct(object):

    def __init__(self, url):
        self.url = url
        self.browser = webdriver.Chrome()
        self.contents = ''
        self.page = 1
        self.total_page = 0
        self.filename = '招行理财产品.xls'
        self.main()

    def main(self):
        self.browser.get(self.url)
        self.get_html()
        self.browser.close()
        print(self.total_page)

    def get_html(self):
        for _i in range(5):
            self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
        self.contents = self.browser.page_source
        self.parse_contents()
        self.total_page += 1
        time.sleep(random.randint(2, 5))
        print('Get next page')
        self.page += 1
        try:
            self.next_page()
        except Exception as e:
            print(e)
            pass

    def next_page(self):
        self.browser.find_element_by_xpath('//div[@class="function"]/a[@href="javascript:loadpage({})"]'.format(self.page)).click()
        self.get_html()

    def parse_contents(self):
        tree = etree.HTML(self.contents)
        div_list = tree.xpath('//div[@class="c_list"]/div[@class="prdBlock"]')
        info_list = []
        try:
            for div in div_list:
                item = dict()
                # 产品代码
                product_id = div.xpath('.//div[@class="cdleftArea"]/div/div[2]/text()')[0]
                item['product_id'] = product_id
                # 产品利率
                interest = div.xpath('.//div[@class="cdleftArea"]/div[2]/div[2]/text()')[0]
                item['interest'] = interest
                # 销售渠道
                channel = div.xpath('.//div[@class="cdleftArea"]/div[3]/div[2]/text()')[0]
                item['channel'] = channel
                # 发售起始日
                start_day = div.xpath('.//div[@class="cdrightArea"]/div/div[2]/text()')[0]
                item['start_day'] = start_day
                # 发售结束日
                end_day = div.xpath('.//div[@class="cdrightArea"]/div[2]/div[2]/text()')[0]
                item['end_day'] = end_day
                # 产品到期日
                due_day = div.xpath('.//div[@class="cdrightArea"]/div[3]/div[2]/text()')[0]
                item['due_day'] = due_day
                # 期限
                duration = div.xpath('.//div[@class="cdrightArea"]/div[3]/div[4]/text()')[0]
                item['duration'] = duration
                info_list.append(item)

        except Exception as e:
            print(e)
            pass

        if os.path.exists(self.filename):
            ExcelUtils.write_to_excel_append(self.filename, info_list)
        else:
            ExcelUtils.write_to_excel(self.filename, '代销国债', info_list)
        print('page {} get'.format(self.total_page))


cmb_url = r'https://www.cmbchina.com/cfweb/CDeposit/Default.aspx'
cmb_china = CmbProduct(cmb_url)

