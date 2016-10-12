
# for x in [0,1,2,3,4,3,2,1,0]:
#     print('{: <{w1}}{:*<{w2}}'.format('', '', w1=4-x, w2=x*2+1))

for x in range(1,10,2):
    print('{:^9}'.format('*'*x))

for x in range(7,0,-2):
    print('{:^9}'.format('*'*x))