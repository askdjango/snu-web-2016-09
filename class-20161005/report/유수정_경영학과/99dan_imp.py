while True :
    number = int(input("구구단 : "))
    for i in range(1,10):
        print("{}x{} = {}".format(number, i, i*number))