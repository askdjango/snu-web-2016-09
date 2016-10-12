message = '노랑 빨강 녹색 파랑 노랑 빨강'
result = {}

for i in message.split():
    if i in result:
        result[i] +=1

    else:
        result[i] = 1


print(result)