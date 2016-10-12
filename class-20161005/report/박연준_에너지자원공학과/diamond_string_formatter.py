''' 과제 2, 형식 지정자를 사용하는 버전,
기존 제출했던 과제물에서는 format_string을 변수화 하지 않고 작성하였다'''

size = 5
longgest_size = size * 2 -1
format_string = '{:^' + str(longgest_size) + '}'

for i in range(1, size+1):
    star_count = i * 2 - 1
    print(format_string.format('*' * star_count))

for i in range(size-1, 0, -1):
    star_count = i * 2 - 1
    print(format_string.format('*' * star_count))
