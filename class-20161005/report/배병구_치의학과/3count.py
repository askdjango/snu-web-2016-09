message = '노랑 빨강 녹색 파랑 노랑 빨강 노랑 빨강'
print(message.split())

d = dict()
for c in message.split():
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
print (d)