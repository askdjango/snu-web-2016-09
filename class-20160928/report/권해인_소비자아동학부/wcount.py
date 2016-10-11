print('[2016 벤처창업웹프로그래밍1] 소비자아동학부, 권해인')
print()

message = str(input('message(띄어쓰기로 구분):'))
wordcount={}
for word in message.split():
        if word in wordcount:
                 wordcount[word]+=1
        else :
                wordcount[word]=1

for word in wordcount:
        print(word,wordcount[word])
