message = '노랑 빨강 녹색 파랑 노랑 빨강 노랑 빨강'
word_list = message.split()
countRed = 0
countYel = 0
countBlu = 0
countGre = 0

for i in range (1,len(word_list)):
    count = 0
    if(word_list[i] == '빨강'):
        countRed += 1
    if(word_list[i] == '노랑'):
        countYel += 1
    if(word_list[i] == '파랑'):
        countBlu += 1
    if(word_list[i] == '녹색'):
        countGre += 1

print(word_list)
print("빨강 : ",countRed)
print("노랑 : ",countYel)
print("파랑 : ",countBlu)
print("녹색 : ",countGre)