width = 5

for i in range(1, width+1):
    s = width - i
    a = i * 2 - 1
    print('{}{}'.format(" "*s, "*"*a))
for i in range(width-1, 0, -1):
    s = width - i
    a = i * 2 - 1
    print('{}{}'.format(" "*s, "*"*a))
