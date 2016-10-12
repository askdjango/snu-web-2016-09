from itertools import count

message = "노랑 빨강 녹색 파랑 노랑 빨강 노랑 빨강"
word_list = message.split()
result = {}


for word in word_list:
    if word in result:
        result[word] += 1
    else:
        result[word] = 1

print(result)