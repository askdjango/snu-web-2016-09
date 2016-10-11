while True:
    number = int(input("몇 단을 알고싶나요?"))
    for i in range(1,10):
        print (number, "X", i,"=",number*i)