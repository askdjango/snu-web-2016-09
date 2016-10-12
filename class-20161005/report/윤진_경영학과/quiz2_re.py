width = 5
width_len = width*2 - 1

format_string = '{:^' + str(width_len) + '}'

for i in range(1, width+1):
    a = i * 2 - 1
    print(format_string.format('*' * a))
for i in range(width-1, 0, -1):
    a = i * 2 - 1
    print(format_string.format('*' * a))