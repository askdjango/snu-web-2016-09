# Previous code
'''
i = 0
while 0 <= i < 5:
    i += 1
    space = ""
    star = ""
    for y in range(5 - i):
        space = space + " "
    for z in range(2 * i - 1):
        star = star + "*"
    print ('{} {}'.format(space, star))
while i >= 0:
    i -= 1
    space = ""
    star = ""
    for y in range(5 - i):
        space = space + " "
    for z in range(2 * i - 1):
        star = star + "*"
    print ('{} {}'.format(space, star))
'''

# Revised code

size = 5

for i in range(1, size+1):
    blank = size - i
    star = 2 * i - 1
    print('{}{}'.format(" " * blank, "*" * star))
for i in range(size-1, 0, -1):
    blank = size - i
    star = 2 * i - 1
    print('{}{}'.format(" " * blank, "*" * star))