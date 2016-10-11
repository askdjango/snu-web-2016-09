number = int(input("구구단 : "))
my_num = [number]
for i in range(1,10):
    my_num.append(i*number)
    print('{}*{}={}'.format(number,i,my_num[i]))