message='노랑 빨강 녹색 파랑 노랑 빨강 노랑 빨강'
dic=message.split()
D={}
for word in dic:
    if word in D:
        D[word] += 1
    else:
        D[word] = 1
for key in D:
    print (key, ':', D[key])