for i in range(0,9):
    if i <= 4:
        print((" "*(4-i)) + ("*"*(2*i+1)) + (" "*(4-i)))
    else:
        print((" "*(i-4)) + ("*"*(17-2*i)) + (" "*(i-4)))


for i in range(0,9):
    if i <= 4:
        print("{}{}{}".format(" "*(4-i), "*"*(2*i+1), " "*(4-i)))
    else:
        print("{}{}{}".format(" "*(i-4), "*"*(17-2*i), " "*(i-4)))