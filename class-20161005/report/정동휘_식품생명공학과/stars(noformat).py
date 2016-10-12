# without format

for i in range(1,10):
    if i < 6:
        stars_num = 2 * i - 1
        stars = '*' * stars_num
        blanks_num = 5 - i
        blanks = ' ' * blanks_num
        print(blanks + stars)
    else:
        stars_num = -2 * ( i - 6 ) + 7
        stars = '*' * stars_num
        blanks_num = i - 5
        blanks = ' ' * blanks_num
        print(blanks + stars)