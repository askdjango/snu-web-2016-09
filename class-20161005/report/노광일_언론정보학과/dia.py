
size = 5
longgest_size = size * 2 - 1

format_string = '{:^' + str(longgest_size) + '}'
# '{:^9}'

for i in range(1, size+1):
    star_count = i * 2 - 1
    print(format_string.format('*' * star_count))

for i in range(size-1, 0, -1):
    star_count = i * 2 - 1
    print(format_string.format('*' * star_count))