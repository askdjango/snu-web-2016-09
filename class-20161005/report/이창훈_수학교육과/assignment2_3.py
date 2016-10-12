for i in range(1,5,+1):
    print('{space}{star}'.format(space = (6-i)*" ", star = (2*i-1)*"*"))

for i in range(5,0,-1):
    print('{space}{star}'.format(space = (6-i)*" ", star = (2*i-1)*"*"))