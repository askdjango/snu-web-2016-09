
#특정 수를 입력받아서, 구구단을 출력하는 프로그램을 작성

number = int(input("구구단 : "))
"""
print("\n %d 단 "%number)
print("----------------")

for i in range(1,10):
    print(" %d x %d = %d" %(number, i, number*i))
print("----------------")
"""

#형식지정자 사용하여 코딩

print("\n {} 단 ".format(number))
print("-"*20)

for i in range(1,10):
    print(" {} x {} = {}".format(number, i, number*i))

print("-"*20)