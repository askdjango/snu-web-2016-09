
#형식 지정자 미사용
num=5
for i in range(num-1):
    print((num-i)*' '+(2*i+1)*'*')
for i in range(num-1, -1, -1):
    print((num-i)*' '+(2*i+1)*'*')


#형식 지정자 사용
num=5
for i in range(num):
    print('{: <{space}}{:*<{star}}'.format('', '', space=num-i-1, star=i*2+1))
for i in range(1, num):
    print('{: <{space}}{:*<{star}}'.format('', '', space=i, star=2*(num-i)-1))
