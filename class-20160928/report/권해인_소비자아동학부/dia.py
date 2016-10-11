print('[2016 벤처창업웹프로그래밍1] 소비자아동학부, 권해인')
print()
number = int(input('몇 층 다이아를 원하십니까?:'))
for i in range(1,2*number,2):
	if i>number:
		i=2*number-i
	print(
		' '*int((number-i)/2),
		'*'*i,
		' '*int((number-i)/2)
	)
