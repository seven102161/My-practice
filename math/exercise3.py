import random


def addition_subtraction(min_, max_):
    count = 25

    print('题目1', ',', '题目2', ',', '答案1', ',', '答案2')
    print()

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

    print('题目1', ',', '题目2', ',', '答案1', ',', '答案2')
    print()

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
            print(x1, 'x', y1, '=', '______', ',', x2, 'x', y2, '=', '______', ',', result1, ',', result2)
            print()
        else:
            print(result1, '÷', x1, '=', '______', ',', result2, '÷', x2, '=', '______', ',', y1, ',', y2)
            print()
        count -= 1


if __name__ == '__main__':
    for _i in range(2):
        addition_subtraction(0, 31)
    for _i in range(2):
        multiplication_division(2, 9)

