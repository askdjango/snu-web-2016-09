# 형식 지정자 사용
for i in range(10):
    diamond = '{}{}'
    if i <= 5:
        spaces = ' ' * (5 - i)
        stars = '*' * (i*2 - 1)
        print(diamond.format(spaces,stars))
    else:
        spaces = ' ' * (i - 5)
        stars = '*' * (19 - i*2)
        print(diamond.format(spaces,stars))