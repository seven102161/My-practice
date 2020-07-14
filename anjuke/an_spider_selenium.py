import time
import os
from selenium import webdriver
from lxml import etree
from excle_wirte import ExcelUtils
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC#seleniunm内置一些条件
from selenium.webdriver.common.by import By


class AnjukeHouse(object):

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()
        self.filename = '弘辉名苑.xls'
        self.main()

    def get_content_by_selenium(self, url):
        #1,创建驱动
        # driver = webdriver.PhantomJS()

        #2请求url
        self.driver.get(url)
        #3、等待
        #强制等待:弊端：死板，而且有的时候还可能等待不够，造成数据的缺失
        # time.sleep(3)
        #隐式等待：相当于页面在等待到转圈圈结束，页面完全加载出来位置。
        #弊端：等待的还是太久了。
        # driver.implicitly_wait(10)#10秒钟还没有全部加载完成的话，就会报超时异常
        #显示等待：可以聚焦到页面中特定元素出现就等待结束。
        # 使用显示等待步骤
        #（1）、创建等待对象
        # 20：显示等待的最大等待时长，20秒还没等待到特定元素加载出来，就报一个超时异常
        #driver:表示这个等待对象监听到那个驱动浏览器程序上
        wait = WebDriverWait(self.driver, 20)
        # （2）用wait对象来进行条件判断
        '''
        EC.presence_of_element_located(定位器)
        定位器是一个元祖(用什么定位器：id,xpath,css,'对应的选择器的语法')
        '''
        wait.until(EC.presence_of_element_located((By.ID, 'houselist-mod-new')))#等到啥时候为止
        # 4、获取页面内容
        return self.driver.page_source

    def parse_li(self, li_list):
        '''
        解析每个div，获取书籍
        :param div_list:
        :return:
        '''
        #存储每一页的数据
        info_list = []
        for li in li_list:
            #异常发生程序终止---当前线程中止
            #规则：异常必须要处理。
            #异常时层层抛出的,所以在处理异常的时候，一定要分析好处理的位置，
            # 这样决定了你是否能利用异常做一些程序的附加功能
            #异常功能：
            try:
                #书籍名称
                house_type = li.xpath('.//div[2]/div[2]/span[1]/text()')[0]
                house_size = li.xpath('.//div[2]/div[2]/span[2]/text()')[0]
                house_total_floor = li.xpath('.//div[2]/div[2]/span[3]/text()')[0]
                house_price = li.xpath('.//div[3]/span[1]/strong/text()')[0]
                house_url = li.xpath('.//div[2]/div[1]/a[1]/@href')

                item = dict()
                item['house_type'] = house_type
                item['house_size'] = house_size
                item['house_total_floor'] = house_total_floor
                item['house_price'] = house_price
                item['house_url'] = house_url
                print(item)
                info_list.append(item)
            except Exception:
                pass

        if os.path.exists(self.filename):
            ExcelUtils.write_to_excel_append(self.filename,info_list)
        else:
            ExcelUtils.write_to_excel(self.filename, '弘辉名苑', info_list)

    def main(self):
        #分页请求
        # for i in range(1):
        i = 1
        while True:
            # print(self.url.format(1))
            html_str = self.get_content_by_selenium(self.url.format(i))
            # print(html_str)
            # 页面内容转成element对象就可以使用xpath语法来进行获取页面内容
            html = etree.HTML(html_str)
            #获取
            li_list = html.xpath('//ul[@id="houselist-mod-new"]/li')
            # print(li_list)
            if not li_list:
                break
            self.parse_li(li_list)
            time.sleep(2)
            i += 1


if __name__ == '__main__':
    #基础url
    base_url = 'https://shanghai.anjuke.com/sale/p{}-rd1/?kw=%E5%BC%98%E8%BE%89%E5%90%8D%E8%8B%91#filtersort'
    AnjukeHouse(base_url)
