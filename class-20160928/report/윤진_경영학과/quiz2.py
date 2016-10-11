width = 5

for i in range(1, width+1):
    for s in range (width - i) :
        print(" ", end="")
    for  a in range((i * 2) - 1):
        print("*", end="")
    print()
for i in range(1, width):
    for s in range (i) :
        print(" ", end="")
    for a in range((width-i)*2 -1):
        print("*", end="")
    print()