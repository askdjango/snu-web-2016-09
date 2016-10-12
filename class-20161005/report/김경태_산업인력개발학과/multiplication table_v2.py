#구구단-함수화
def myfn(a):
    for i in range(1, 10):
        print(a,'x',i,'=',a*i)

while 1:
    num=int(input("몇 단을 원하시나요?:"))
    if num < 10 and num >= 1:
        break
    else:
        print('다시 골라주세요.')

myfn(num)