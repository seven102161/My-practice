import random


def addition_subtraction(min_, max_):
    count = 25

    while count > 0:
        x1 = random.randint(min_, max_)
        y1 = random.randint(min_, max_)
        x2 = random.randint(min_, max_)
        y2 = random.randint(min_, max_)
        if y1 > x1 or y2 > x2:
            continue
        sym_list = ['1', '2']
        sym = random.choice(sym_list)
        if sym == '1':
            result1 = x1 + y1
            result2 = x2 + y2
            print(x1, '+', y1, '=', '______', ',', x2, '+', y2, '=', '______', ',', result1, ',', result2)
            print()

        else:
            result1 = x1 - y1
            result2 = x2 - y2
            print(x1, '-', y1, '=', '______', ',', x2, '-', y2, '=', '______', ',', result1, ',', result2)
            print()

        count -= 1


def multiplication_division(min_, max_):
    count = 25

    # print('题目1', ',', '题目2', ',', '答案1', ',', '答案2')

    while count > 0:
        x1 = random.randint(min_, max_)
        y1 = random.randint(min_, max_)
        x2 = random.randint(min_, max_)
        y2 = random.randint(min_, max_)

        result1 = x1 * y1
        result2 = x2 * y2

        sym_list = ['3', '4']
        sym = random.choice(sym_list)

        if sym == '3':
            ques = f'{x1} x {y1} = ______,{x2} x {y2} = ______,{result1},{result2}\n'
        else:
            ques = f'{result1} ÷ {x1} = ______,{result2} ÷ {x2} = ______,{y1},{y2}\n'

        count -= 1
        return ques


if __name__ == '__main__':
    with open('abc.csv', 'w') as f:
        for _i in range(2):
            line1 = f'乘除,page{_i + 1},,page{_i + 1}\n'
            f.write(line1)
            f.write(multiplication_division(3, 9))
        f.close()
    # for _i in range(2):
    #     print('加减', ',', 'page', _i + 1, ',', ',', 'page', _i + 1)
    #     print()
    #     addition_subtraction(0, 31)
    # for _i in range(2):
    #     print('乘除', ',', 'page', _i + 1, ',', ',', 'page', _i + 1)
    #     print()
    #     multiplication_division(3, 9)

