# 과제 2, 형식 지정자를 사용하지 않는 버전
size = 5

for i in range(1, size+1):
    blank_count = size - i
    star_count = i * 2 - 1
    print(' ' * blank_count, end='')
    print('*' * star_count)

for i in range(size-1, 0, -1):
    blank_count = size - i
    star_count = i * 2 - 1
    print(' ' * blank_count, end='')
    print('*' * star_count)
