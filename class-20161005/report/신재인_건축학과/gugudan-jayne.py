number = int(input("구구단 숫자를 입력하시오 : "))

for i in range(1,10) :
    print ( '%d단 : ' %i , end= ' ')
    print ( i* number )

