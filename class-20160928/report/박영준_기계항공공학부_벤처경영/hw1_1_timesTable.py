number = int(input("구구단: "))

for n in range(0,10):
    timesTable = ' {} x {} = {}'.format(number,n,number*n)
    print(timesTable)