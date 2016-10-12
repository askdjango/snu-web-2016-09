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
    print (space, star)
while i >= 0:
    i -= 1
    space = ""
    star = ""
    for y in range(5 - i):
        space = space + " "
    for z in range(2 * i - 1):
        star = star + "*"
    print (space, star)
    '''

# Revised code

size = 5
i = 0
while 0 <= i < 5:
    i += 1
    space = size - i
    star = 2 * i - 1
    print(' ' * space, end='')
    print('*' * star)
while i >= 0:
    i -= 1
    space = size - i
    star = 2 * i - 1
    print(' ' * space, end='')
    print('*' * star)