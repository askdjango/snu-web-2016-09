print('1부터 9까지의 숫자를 입력하세요.')
i = 10
while i <13 :
	number = int(input('구구단 : '))
	if number<10 :
		for i in range(1,10) :
			print(number,'x',i, '=',number*i)
	elif number >= 10 :
		print('안됩니다. 돌아가세요. 1부터 9까지만 가르쳐줄거에요.다시 입력해요.')
		
		

		'''
print('2부터 9까지의 숫자를 입력하세요. 알파벳 a를 입력하시면 자동으로 프로그램이 종료됩니다.')


while True:
	number = int(input('구구단 : '))
	for i in range(1,10):
		print(number,'x',i, '=', number*i
'''