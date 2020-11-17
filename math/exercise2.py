import random

count = 25
num = 0

print('题目', ',', '答案')
print()

while count > 0:
    x = random.randint(2, 9)
    y = random.randint(2, 9)

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

