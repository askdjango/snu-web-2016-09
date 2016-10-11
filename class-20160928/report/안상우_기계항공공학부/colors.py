message='노랑 빨강 녹색 파랑 노랑 빨강 노랑 빨강'
i=message.split()
j={}
for w in i:
    if w in j:
        j[w] += 1
    else:
        j[w] = 1
for a in j:
    print (a, ':', j[a])