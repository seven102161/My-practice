import requests
import time
from bs4 import BeautifulSoup
import json
import xlwt
import xlrd
from xlutils.copy import copy as C


class CrawlerTool(object):

    @staticmethod
    def write_to_json(file_name, _list):
        with open(file_name, 'w', encoding='utf-8') as fp:
            json.dump(_list, fp)
        print('写入成功！')

    @staticmethod
    def get_proxy(page=1):
        base_url = 'https://www.kuaidaili.com/free/inha/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
            'Referer': 'https://www.kuaidaili.com/free/inha/1/',
        }
        proxy_list = []
        for i_ in range(page):
            full_url = base_url + str(i_ + 1)
            print(f'get proxy ip, page: {i_ + 1}')
            response = requests.get(full_url, headers=headers)
            soup_p = BeautifulSoup(response.text, features='html.parser')
            t_body = soup_p.select('#list > table > tbody')[0]
            trs = t_body.find_all('tr')
            for tr in trs:
                ip = tr.find('td', {'data-title': "IP"}).text
                port = tr.find('td', {'data-title': "PORT"}).text
                proxy = 'http://' + ip + ':' + port
                print(proxy)
                proxy_list.append(proxy)
            print('get proxy ip:', len(proxy_list))
            if page > 1:
                time.sleep(10)
        return proxy_list

    @staticmethod  # 类方法
    def write_to_excel(filename, sheet_name, word_list):
        '''
        写入excel
        :param filename: 文件名
        :param sheet_name: 表单名
        :param word_list: [item,item,{}]
        :return:
        '''
        try:
            # 创建workbook
            workbook = xlwt.Workbook(encoding='utf-8')
            # 给工作表添加sheet表单
            sheet = workbook.add_sheet(sheet_name)
            # 设置表头
            head = []
            for i in word_list[0].keys():
                head.append(i)

            # 将表头写入excel
            for i in range(len(head)):
                sheet.write(0, i, head[i])  # 第0行，第i列，第i列表头

            # 写内容
            i = 1
            for item in word_list:
                for j in range(len(head)):
                    sheet.write(i, j, item[head[j]])  # 第i行（第1行起），第j列，第j列key的内容
                i += 1
            # 保存
            workbook.save(filename)
            print('写入excle成功！')
        except Exception as e:
            print(e)
            print('写入失败！')

    @staticmethod
    def write_to_excel_append(filename, infos):
        '''
        追加excel的方法
        :param filename: 文件名
        :param infos: [item，item]
        :return:
        '''

        # 打开excle文件
        work_book = xlrd.open_workbook(filename)
        # 获取工作表中的所有sheet表单名称
        sheets = work_book.sheet_names()
        # 获取第一个表单
        work_sheet = work_book.sheet_by_name(sheets[0])
        # 获取已经写入的行数
        old_rows = work_sheet.nrows
        # 获取表头的所有字段
        keys = work_sheet.row_values(0)
        # print('===================',keys)
        # 将xlrd对象转化成xlwt，为了写入
        new_work_book = C(work_book)
        # 获取表单来添加数据
        new_sheet = new_work_book.get_sheet(0)
        i = old_rows
        for item in infos:
            for j in range(len(keys)):
                new_sheet.write(i, j, item[keys[j]])
            i += 1

        new_work_book.save(filename)
        print('追加成功！')
