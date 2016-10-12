# with format

size = 9

format_string = '{:^'+str(size)+'}'

for i in range(1,10):
    if i < 6:
        stars_num = 2 * i - 1
    else:
        stars_num = -2 * ( i - 6 ) + 7
    print(format_string.format('*'*stars_num))