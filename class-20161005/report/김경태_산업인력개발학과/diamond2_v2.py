# 다이아몬드 형식O-함수화

#숫자가 정해진 경우

def myfn():
    num=5
    for i in range(num):
        print('{: <{space}}{:*<{star}}'.format('', '', space=num-i-1, star=i*2+1))
    for i in range(1, num):
        print('{: <{space}}{:*<{star}}'.format('', '', space=i, star=2*(num-i)-1))
myfn()

# 숫자를 입력 받는 경우
'''
num = int(input('숫자를 입력하세요:'))
def myfn(a):
    for i in range(a):
        print('{: <{space}}{:*<{star}}'.format('', '', space=a-i-1, star=i*2+1))
    for i in range(1, a):
        print('{: <{space}}{:*<{star}}'.format('', '', space=i, star=2*(a-i)-1))

myfn(num)
'''