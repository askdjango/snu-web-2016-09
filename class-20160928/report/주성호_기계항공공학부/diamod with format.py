num_st = [1,3,5,7,9,7,5,3,1]
num_sp = [4,3,2,1,0,1,2,3,4]
i=0
while i<9:
    print('{}{}'.format(num_sp[i]*' ',num_st[i]*'*'), end="")
    print('\n')
    i +=1
