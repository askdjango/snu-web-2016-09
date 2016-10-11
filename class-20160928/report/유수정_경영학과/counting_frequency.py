
message = input('메세지를 입력하세요. 단, 단어 사이 띄어쓰기를 해주셔야 해요 :) >>  ')
print(message.split())
list1 = message.split()
number1 = len(list1)

i = input('빈도수를 세고 싶은 특정 단어를 입력하세요. >> ')
while True :
	if i in list1 :
		list1.remove(i)
	else :
		break
number2 = len(list1)
frequency = number1 - number2
print('메세지 속에 "{}"이(가) 총 {}번 포함 되어있어요.'.format(i,frequency))

