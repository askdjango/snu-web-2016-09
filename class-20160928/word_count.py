message = '노랑 빨강 녹색 파랑 노랑 빨강 노랑 빨강'

result = {}

for word in message.split():
    if word in result:
        result[word] += 1
    else:
        result[word] = 1

print(result)


# 노랑 : 3
# 빨강 : 3
# 녹색 : 1
# 파랑 : 1
