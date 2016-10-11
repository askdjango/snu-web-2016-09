message = '노랑 빨강 녹색 파랑 노랑 빨강 노랑 빨강'
print(message.split())
#To input a color that we want to count, put the 'str(input())' statement
Color = str(input("Color : "))
#The number of count starts at 0
count = 0
# using the 'for' and 'if' to count the designated color
for word in message.split():
    if word == Color:
# if the condition is satisfied, count increases one by one
        count += 1
# print the result, 'count'
print (count)