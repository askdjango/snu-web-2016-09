number = int(input("구구단 : "))
for i in range (1,10):
    print(("{number}*{i} = %d" %(number*i)).format(number=number,i=i))