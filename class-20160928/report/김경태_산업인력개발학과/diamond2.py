num=5
for i in range(num):
    print('{: <{space}}{:*<{star}}'.format('', '', space=num-i-1, star=i*2+1))
for i in range(1, num):
    print('{: <{space}}{:*<{star}}'.format('', '', space=i, star=2*(num-i)-1))