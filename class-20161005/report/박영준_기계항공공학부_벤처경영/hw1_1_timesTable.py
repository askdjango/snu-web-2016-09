number = int(input("구구단: "))

print("\n구구단 {}단\n".format(number))
for n in range(1,10):
    timesTable = ' {} x {} = {}'.format(number,n,number*n)
    print(timesTable)