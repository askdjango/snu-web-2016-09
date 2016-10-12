size = 5

for i in range(1, size+1):
    blank_count = size - i   #빈칸 숫자 /
    star_count = i * 2 - 1
    print(' ' * blank_count, end='')   # end='' 안 쓰면 줄 넘어감
    print('*' * star_count)

for i in range(size-1, 0, -1):
    blank_count = size - i
    star_count = i * 2 - 1
    print(' ' * blank_count, end='')
    print('*' * star_count)