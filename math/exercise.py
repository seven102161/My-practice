import random

count = 25
num = 0

print('题目', ',', '答案')
print()

while count > 0:
    x = random.randint(0, 21)
    y = random.randint(0, 21)
    if y > x:
        continue
    sym_list = ['+', '-']
    sym = random.choice(sym_list)
    if sym == '+':
        result = x + y
        print(x, '+', y, '=', '______', ',', result)
        print()
    else:
        result = x - y
        print(x, '-', y, '=', '______', ',', result)
        print()
    count -= 1

