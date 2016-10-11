# 형식 지정자를 사용하는 star diamond 출력

star = '*'

for i in range(1, 10, 2):
    print("{0:^9}".format(star*i))

for j in range(7, 0, -2):
    print("{0:^9}".format(star*j))
