# 형식 지정자를 사용하지 않는 star diamond 출력

star = '*'

n = 4
for i in range(1, 10, 2):
    print(' '*n + star*i)
    n -= 1

n = 1
for j in range(7, 0, -2):
    print(' '*n + star*j)
    n += 1
