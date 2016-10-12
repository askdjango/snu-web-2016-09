message = input('메세지를 입력하세요. >>  ')

result = {}
#result = {}는 result가 사전이라는 '성격 정의'를 하는 것이므로 꼭 필요한 문장!

for word in message.split():
    if word in result:
        result[word] += 1
    else:
        result[word] = 1

print(result)
