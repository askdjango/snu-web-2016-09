number = int(input("출력하고자 하는 구구단의 숫자를 입력하세요. 1단부터 9단까지 가능합니다. : "))

while number < 1 or number > 9 :
    number = int(input("1단부터 9단까지만 출력가능합니다. 1 이상 9이하의 숫자를 입력하세요."))

for x in range (1,10) :
    print(number, 'x',x,'=',number*x)

