# Previous code
'''
message = '노랑 빨강 녹색 파랑 노랑 빨강 노랑 빨강'
print(message.split())
Color = str(input("Color : "))
count = 0
for word in message.split():
    if word == Color:
        count += 1
print (count)                   # Describing the number of input word
'''

# Revised code


message = '노랑 빨강 녹색 파랑 노랑 빨강 노랑 빨강'
print(message.split(),'\n')

result = {}

for word in message.split():
    if word in result:
        result[word] += 1
    else:
        result[word] = 1

print(result) # Describing all the number of each recorded word