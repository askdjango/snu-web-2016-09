
#다이아몬드를 출력하는 코드의 여러 버전 작성

#형식 지정자를 사용하지 않은 버전
print("# 형식 지정자를 사용하지 않은 버전")
star = "*"
blank = " "

for i in range(4,-1,-1):
    print(blank*i + star*(9-i*2) + blank*i)
for i in range(1,5):
    print(blank*i + star*(9-i*2) + blank*i)

print("\n")

#형식 지정자를 사용한 버전
print("# 형식 지정자를 사용한 버전")
for i in range(4,-1,-1):
    print('{0}{1}{0}'.format(blank*i, star*(9-i*2)))
for i in range(1,5):
    print('{0}{1}{0}'.format(blank*i, star*(9-i*2)))


#다이아몬드의 길이를 지정할 수 있는 버전
print("\n# 다이아몬드의 총 길이(홀수)를 지정할 수 있는 버전")
number = int(input("다이아몬드의 길이를 홀수로 입력하세요 : "))

while number%2==0:
    number = int(input("홀수로 입력하세요 : "))

a = int((number-1)/2)

for i in range(a,-1,-1):
    print('{0}{1}{0}'.format(blank*i, star*(number-i*2)))
for i in range(1,a+1):
    print('{0}{1}{0}'.format(blank*i, star*(number-i*2)))



#다이아몬드의 size 받아서 다이아몬드 출력
print("\n# 다이아몬드의 size 받아서 다이아몬드 출력")
size = int(input("다이아몬드의 size를 입력하세요 : "))

while size<0:
    size = int(input("0 이상의 정수의 유효한 size를 입력하세요 : "))

len = size*2-1
blank_cnt = size-1

for i in range(blank_cnt,-1,-1):
    print('{0}{1}{0}'.format(blank*i, star*(len-i*2)))
for i in range(1,size):
    print('{0}{1}{0}'.format(blank*i, star*(len-i*2)))




#중앙 정렬 활용하여 다이아몬드 출력
print("\n# 다이아몬드의 size 받아 중앙 정렬 활용하여 다이아몬드 출력")
size = int(input("다이아몬드의 size를 입력하세요 : "))

while size<0:
    size = int(input("0 이상의 정수의 유효한 size를 입력하세요 : "))

len = size*2-1
format_string = '{:^' + str(len) + '}'

for i in range(1,len+1,2):
    print(format_string.format(star*i))
for i in range(len-2,0,-2):
    print(format_string.format(star*i))

