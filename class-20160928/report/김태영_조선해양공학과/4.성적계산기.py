result = {} 


for i in range(1, 4): 
	name = input('{} 번째 학생 이름은? '.format(i)) 
	ko_score = input('{}님의 국어 시험 점수는? '.format(name)) 
	en_score = input('{}님의 영어 시험 점수는? '.format(name)) 
	math_score = input('{}님의 수학 시험 점수는? '.format(name)) 
	result[name] = { 
		'ko_score': ko_score, 
		'en_score': en_score, 
		'math_score': math_score, 
	} 


print('개별 평균점수') 
for name in result: 
	

	print('[{}] 국어: {}, 영어: {}, 수학: {}') 


print('전체 국어 평균점수는?')  # TODO: 계산하세요. 
print('전체 영어 평균점수는?')  # TODO: 계산하세요. 
print('전체 수학 평균점수는?')  # TODO: 계산하세요. 

n=input('{}'.format())