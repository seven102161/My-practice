import random
import pandas as pd
import openpyxl
from xlwt import Workbook


def addition_subtraction(min_, max_):
    x = random.randint(min_, max_)
    y = random.randint(min_, max_)
    sym_list = ['1', '2']
    sym = random.choice(sym_list)
    if sym == '1':
        res = x + y
        ques = '{} + {} = ______'.format(x, y)
        ans = str(res)
    else:
        if x > y:
            res = x - y
            ques = '{} - {} = ______'.format(x, y)
            ans = str(res)
        else:
            res = y - x
            ques = '{} - {} = ______'.format(y, x)
            ans = str(res)
    return ques, ans


def multiplication_division(min_, max_):
    x = random.randint(min_, max_)
    y = random.randint(min_, max_)
    sym_list = ['3', '4']
    sym = random.choice(sym_list)
    res = x * y
    if sym == '3':
        ques = '{} x {} = ______'.format(x, y)
        ans = str(res)
    else:
        ques = '{} ÷ {} = ______'.format(res, x)
        ans = str(y)

    return ques, ans


def ques_add():
    lst_ques1 = list()
    lst_ques2 = list()
    lst_ques3 = list()
    lst_ques4 = list()
    for _i in range(25):
        lst_ques1.append(' ')
        lst_ques1.append(addition_subtraction(3, 30)[0])
        lst_ques2.append(' ')
        lst_ques2.append(addition_subtraction(3, 30)[0])
        lst_ques3.append(' ')
        lst_ques3.append(addition_subtraction(3, 30)[0])
        lst_ques4.append(' ')
        lst_ques4.append(addition_subtraction(3, 30)[0])

    data = dict()
    data['题目1'] = lst_ques1
    data['题目2'] = lst_ques2
    data['题目3'] = lst_ques3
    data['题目4'] = lst_ques4

    index = [i + 1 for i in range(len(lst_ques1))]
    df = pd.DataFrame(data=data, index=index)
    return df


def ques_multi():
    lst_ques1 = list()
    lst_ques2 = list()
    lst_ques3 = list()
    lst_ques4 = list()
    for _i in range(25):
        lst_ques1.append(' ')
        lst_ques1.append(multiplication_division(3, 9)[0])
        lst_ques2.append(' ')
        lst_ques2.append(multiplication_division(3, 9)[0])
        lst_ques3.append(' ')
        lst_ques3.append(multiplication_division(3, 9)[0])
        lst_ques4.append(' ')
        lst_ques4.append(multiplication_division(3, 9)[0])

    data = dict()
    data['题目1'] = lst_ques1
    data['题目2'] = lst_ques2
    data['题目3'] = lst_ques3
    data['题目4'] = lst_ques4

    index = [i + 1 for i in range(len(lst_ques1))]
    df = pd.DataFrame(data=data, index=index)
    return df


if __name__ == '__main__':
    df1 = ques_add()
    print(df1)
    df2 = ques_multi()
    print(df2)
    writer = pd.ExcelWriter('C:\\Users\\admin\\Desktop\\math.xlsx')
    df1.to_excel(writer, columns=['题目1', '题目2', '题目3', '题目4'],
                 index=False, encoding='utf-8', sheet_name='Sheet1')
    df2.to_excel(writer, columns=['题目1', '题目2', '题目3', '题目4'],
                 index=False, encoding='utf-8', sheet_name='Sheet2')
    writer.save()
    writer.close()
