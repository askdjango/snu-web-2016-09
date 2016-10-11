# 형식 지정자 미사용
for i in range(10):
    if i <= 5:
        spaces = 5 - i
        stars = i*2 - 1
        print(" "*spaces + "*"*stars)
    else:
        spaces = i - 5
        stars = 19 - i*2
        print(" "*spaces + "*"*stars)