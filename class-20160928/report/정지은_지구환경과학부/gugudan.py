j = 0
while j<10:

    number = int(input("구구단 몇 단을 원해?"))

    for i in range(1, 10) :
        print(number,'*',i,'=',number*i)

    j = j+1

