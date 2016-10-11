# Not able to code the question in one conditional statement, then use 'while' in two statements
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