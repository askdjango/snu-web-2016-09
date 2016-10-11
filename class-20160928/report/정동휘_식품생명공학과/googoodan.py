number = int(input("구구단: "))
if number < 10 and 1 < number:
    for i in range(1,10):
        result = number*i
        print('{a} * {b} = {c}'.format(a=str(number), b=str(i), c=str(result)))
else:
    print("구구단은 2부터 9까지입니다 :)")