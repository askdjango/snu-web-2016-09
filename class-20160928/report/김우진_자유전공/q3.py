message = '노랑 빨강 녹색 파랑 노랑 빨강 노랑 빨강 '
file = message.split()
wordcount={}
for word in file:
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
print (word,wordcount)