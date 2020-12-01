import random
import xlwt


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
        lst_ques1.append(addition_subtraction(3, 30)[0])
        lst_ques2.append(addition_subtraction(3, 30)[0])
        lst_ques3.append(addition_subtraction(3, 30)[0])
        lst_ques4.append(addition_subtraction(3, 30)[0])

    data = dict()
    data['题目1'] = lst_ques1
    data['题目2'] = lst_ques2
    data['题目3'] = lst_ques3
    data['题目4'] = lst_ques4

    return data


def ques_multi():
    lst_ques1 = list()
    lst_ques2 = list()
    lst_ques3 = list()
    lst_ques4 = list()
    for _i in range(25):
        # lst_ques1.append(' ')
        lst_ques1.append(multiplication_division(3, 9)[0])
        # lst_ques2.append(' ')
        lst_ques2.append(multiplication_division(3, 9)[0])
        # lst_ques3.append(' ')
        lst_ques3.append(multiplication_division(3, 9)[0])
        # lst_ques4.append(' ')
        lst_ques4.append(multiplication_division(3, 9)[0])

    data = dict()
    data['题目1'] = lst_ques1
    data['题目2'] = lst_ques2
    data['题目3'] = lst_ques3
    data['题目4'] = lst_ques4

    return data


def write_to_excel(sheet_name, ques_data):
    global workbook
    # 给工作表添加sheet表单
    worksheet = workbook.add_sheet(sheet_name)
    # 格式设置
    style = xlwt.XFStyle()
    # 设置字体样式
    font = xlwt.Font()
    font.name = '宋体'
    font.height = 20 * 12
    style.font = font
    # 设置表头
    head = ['题目1', '题目2', '题目3', '题目4']

    # 将表头写入excel
    for _j in range(len(head)):
        worksheet.write(0, _j, head[_j], style)  # 第0行，第i列，第i列表头
        # 设置列宽
        worksheet.col(_j).width = 18 * 256

    for _j in range(len(head)):
        q_data = ques_data
        q_list = q_data[head[_j]]
        for _i in range(len(q_list)):
            worksheet.write(_i + 1, _j, q_list[_i], style)
            # 设置单元格高度
            worksheet.row(_i + 1).height_mismatch = True
            worksheet.row(_i + 1).height = 600


if __name__ == '__main__':
    # 创建workbook
    workbook = xlwt.Workbook(encoding='utf-8')
    # 写入法减法sheet
    write_to_excel('加减法', ques_add())
    # 写入乘除法sheet
    write_to_excel('乘除法', ques_multi())
    workbook.save('/Users/jiangzhiyi/Desktop/math.xls')
