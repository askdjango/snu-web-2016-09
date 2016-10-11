print("과제 3번")

message = '노랑 빨강 녹색 파랑 노랑 빨강 노랑 빨강'

print(message.split())

count={}

for word in message.split():
	if word not in count:
		count[word]=1
	else:
		count[word]=count[word]+1

print(count.items())

message1 = int(input("끝")) 
	