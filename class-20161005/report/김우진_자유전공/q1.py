


number = int(input("몇단이 궁금하신가요? : "))
aa = range(1,10)

if number >= 10:
    print('9단까지만 지원합니다.')

elif number > 0:
    for i in aa:
        print(number, " * ", i, " = ", number * i)

else:
    print('%d is wrong number.' % number)


