#과제 2-1번.
print('과제 2-1번을 시작합니다.')
a='*'
space=' '
for i in range(1,10):
    if i<6:
        b=2*i-1
        c=5-i
        print(c*space,a*b)
    else:
        b=19-(2*i)
        c=i-5
        print(c*space,a*b)
print('2-1completed, without 형식지정자.')

print('과제 2-2번을 시작합니다.')
a='    *********' #space4, star9
for i in range(0,9):
    if i<5:
        print('%s' %(a[i:2*i+5]))
    else:
        print('%s' %(a[8-i:21-2*i]))

print('2-2completed, with 형식지정자')