#과제 3번.
print('과제 3번을 시작합니다.')
sentence = str(input('문장을 입력하세요 : ')) #예를 들면 '노랑 빨강 녹색 파랑 노랑 빨강 노랑 빨강'
words={}

for word in sentence.split():
	if word in words:
		words[word]+=1
	else:
		words[word]=1
print(words)