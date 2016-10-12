# 구구단

number = int(input("구구단 : "))

if 1 < number & number < 10:
    for i in range(1,10):
        result = number * i
        print("%d * %d = %d" % (number, i, result))
else:
    print("구구단은 2부터 9까지입니다.")