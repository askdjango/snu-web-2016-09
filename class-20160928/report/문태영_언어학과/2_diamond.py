
#다이아몬드를 출력하는 코드의 2가지 버전 작성

#형식 지정자를 사용하지 않은 버전
star = "*"
blank = " "

for i in range(4,-1,-1):
    print(blank*i + star*(9-i*2) + blank*i)
for i in range(1,5):
    print(blank*i + star*(9-i*2) + blank*i)

print("\n")

#형식 지정자를 사용한 버전
for i in range(4,-1,-1):
    print('{0}{1}{0}'.format(blank*i, star*(9-i*2)))
for i in range(1,5):
    print('{0}{1}{0}'.format(blank*i, star*(9-i*2)))

"""
#다이아몬드의 길이를 지정할 수 있는 버전

number = int(input("다이아몬드의 길이를 홀수로 입력하세요 : "))

while number%2==0:
    number = int(input("홀수로 입력하세요 : "))

a = int((number-1)/2)

for i in range(a,-1,-1):
    print('{0}{1}{0}'.format(blank*i, star*(number-i*2)))
for i in range(1,a+1):
    print('{0}{1}{0}'.format(blank*i, star*(number-i*2)))
"""