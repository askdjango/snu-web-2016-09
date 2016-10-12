#과제 2-1번.
print('과제 2-1번을 시작합니다.')
a='    *********' #space4, star9
for i in range(0,9):
    if i<5:
        print(a[i:2*i+5])
    else:
        print(a[8-i:21-2*i])
print('형식지정자 미사용 과제 끝.')

print('과제 2-2번을 시작합니다.')
a='*' 
for i in range(0,9):
    if i<5:
        print('{:^9}'.format((2*i+1)*a))
    else:
        print('{:^9}'.format((17-2*i)*a))
print('형식지정자 사용 과제 끝.')
