#다이아몬드 형식X-함수화
# 숫자가 정해진 경우,

def myfn():
    num=5
    for i in range(num-1):
        print((num-i)*' '+(2*i+1)*'*')
    for i in range(num-1, -1, -1):
        print((num-i)*' '+(2*i+1)*'*')

myfn()

# 숫자를 입력받는 경우,

'''
num = int(input('숫자를 입력하세요:'))

def myfn(a):
    for i in range(a-1):
        print((a-i-1)*' '+(2*i+1)*'*')
    for i in range(a-1, -1, -1):
        print((a-i-1)*' '+(2*i+1)*'*')

myfn(num)
'''