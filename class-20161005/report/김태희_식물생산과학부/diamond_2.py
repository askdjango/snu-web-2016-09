size = int(input("size 입력하세요 : "))
width = size * 2 - 1

for i in range(1, size+1):
    space = size - i
    star = i * 2 - 1
    print(' ' * space, end = '')
    print('*' * star)

for i in range(size-1, 0, -1):
    space = size - i
    star = i * 2 - 1
    print(' ' * space, end = '')
    print('*' * star)