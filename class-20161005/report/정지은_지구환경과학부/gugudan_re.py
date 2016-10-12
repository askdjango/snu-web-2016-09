print("※ 당신은 구구단을 10번 검색할 기회가 주어집니다.")

j = 0
while j<10:

    number = int(input("구구단 몇 단을 원해?"))

    for i in range(1, 10) :
        print('{} * {} = {}'.format(number, i, number * i))

    j = j+1