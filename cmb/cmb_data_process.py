import json
import re
from excle_wirte import ExcelUtils


def make_product_list(info_list):
    product_list = []
    for info in info_list:
        item = dict()
        PrdCode = re.search(r'PrdCode:"(.*?)"', info, re.S).group(1)
        item['PrdCode'] = PrdCode

        PrdName = re.search(r'PrdName:"(.*?)"', info, re.S).group(1)
        item['PrdName'] = PrdName

        TypeCode = re.search(r'TypeCode:"(.*?)"', info, re.S).group(1)
        item['TypeCode'] = TypeCode

        Currency = re.search(r'Currency:"(.*?)"', info, re.S).group(1)
        item['Currency'] = Currency

        BeginDate = re.search(r'BeginDate:"(.*?)"', info, re.S).group(1)
        item['BeginDate'] = BeginDate

        EndDate = re.search(r'EndDate:"(.*?)"', info, re.S).group(1)
        item['EndDate'] = EndDate

        ExpireDate = re.search(r'ExpireDate:"(.*?)"', info, re.S).group(1)
        item['ExpireDate'] = ExpireDate

        Status = re.search(r'Status:"(.*?)"', info, re.S).group(1)
        item['Status'] = Status

        Term = re.search(r'Term:"(.*?)"', info, re.S).group(1)
        item['Term'] = Term

        Style = re.search(r'Style:"(.*?)"', info, re.S).group(1)
        item['Style'] = Style

        InitMoney = re.search(r'InitMoney:"(.*?)"', info, re.S).group(1)
        item['InitMoney'] = InitMoney

        IncresingMoney = re.search(r'IncresingMoney:"(.*?)"', info, re.S).group(1)
        item['IncresingMoney'] = IncresingMoney

        Risk = re.search(r'Risk:"(.*?)"', info, re.S).group(1)
        item['Risk'] = Risk

        FinDate = re.search(r'FinDate:"(.*?)"', info, re.S).group(1)
        item['FinDate'] = FinDate

        SaleChannel = re.search(r'SaleChannel:"(.*?)"', info, re.S).group(1)
        item['SaleChannel'] = SaleChannel

        SaleChannelName = re.search(r'SaleChannelName:"(.*?)"', info, re.S).group(1)
        item['SaleChannelName'] = SaleChannelName

        interest = re.search(r'ShowExpectedReturn:"(.*?)"', info, re.S).group(1)
        item['interest'] = interest

        print(item)
        product_list.append(item)

    return product_list


def write_to_json(product_list):
    with open('cmb_data.json', 'w', encoding='utf-8') as fp:
        json.dump(product_list, fp)
    print('done json')


def write_to_excel(product_list):
    ExcelUtils.write_to_excel('招行理财产品.xls', '代销国债', product_list)
    print('done xls')


def main(info_list):
    product_list = make_product_list(info_list)
    # print(product_list)
    write_to_json(product_list)
    write_to_excel(product_list)


if __name__ == '__main__':
    data = open('cmb_data_original.json').read()
    info_list = json.loads(data)
    # for i in info_list[:3]:
    #     print(i)
    main(info_list)
