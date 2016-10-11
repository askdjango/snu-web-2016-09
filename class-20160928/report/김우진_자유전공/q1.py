


number = int(input("구구단 : "))
aa = [1, 2, 3, 4, 5, 6, 7, 8, 9]

if number > 0:
    for i in aa:
        print(number, " * ", i, " = ", number * i)


else:
    print('%d is wrong number.' % number)


