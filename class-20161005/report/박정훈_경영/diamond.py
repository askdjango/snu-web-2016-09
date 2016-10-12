for i in range(1,5*2,2):
    print((" "*((5*2-1-i)//2))+("*"*i))

for j in range(5*2-3,0,-2):
    print((" "*((5*2-1-j)//2))+"*"*j)


for i in range(1,5*2,2):
    print('{}{}'.format(" "*((5*2-1-i)//2),"*"*i))

for j in range(5*2-3,0,-2):
    print('{}{}'.format(" "*((5*2-1-j)//2),"*"*j))