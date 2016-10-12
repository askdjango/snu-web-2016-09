message = '노랑 빨강 녹색 파랑 노랑 빨강 노랑 빨강'

counter = {}

message_split = message.split()

for color in message_split:
    if color not in counter:
        counter[color] = 1
    else:
        counter[color] += 1

print('메시지: '+message)
print('단어별 등장 횟수: '+str(counter))