import random


def addition_subtraction(min_, max_):
    count = 25

    print('题目', ',', '答案')
    print()

    while count > 0:
        x = random.randint(min_, max_)
        y = random.randint(min_, max_)
        if y > x:
            continue
        sym_list = ['1', '2']
        sym = random.choice(sym_list)
        if sym == '1':
            result = x + y
            print(x, '+', y, '=', '______', ',', result)
            print()
        else:
            result = x - y
            print(x, '-', y, '=', '______', ',', result)
            print()
        count -= 1


def multiplication_division(min_, max_):
    count = 25

    print('题目', ',', '答案')
    print()

    while count > 0:
        x = random.randint(min_, max_)
        y = random.randint(min_, max_)

        result = x * y

        sym_list = ['3', '4']
        sym = random.choice(sym_list)
        if sym == '3':
            print(x, 'x', y, '=', '______', ',', result)
            print()
        else:
            print(result, '÷', x, '=', '______', ',', y)
            print()
        count -= 1


if __name__ == '__main__':
    # for _i in range(2):
    #     addition_subtraction(0, 31)
    for _i in range(2):
        multiplication_division(2, 9)

