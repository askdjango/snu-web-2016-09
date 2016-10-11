result = {}

for i in range(1, 4):
    name = input('{} 번째 학생 이름은? '.format(i))
    ko_score = input('{}님의 국어 시험 점수는? '.format(name))
    en_score = input('{}님의 영어 시험 점수는? '.format(name))
    math_score = input('{}님의 수학 시험 점수는? '.format(name))
    result[name] = {
        'ko_score': ko_score,
        'en_score': en_score,
        'math_score': math_score
		}


for name in result : 
	result[name]['per_avg']=(int(result[name]['ko_score'])+int(result[name]['en_score'])
	+int(result[name]['math_score']))/3
	print('[{}] 국어: {}, 영어: {}, 수학: {}'.format(name, int(result[name]
	['ko_score']),int(result[name]['en_score']), int(result[name]['math_score'])))
	print('개별 평균점수 : {}'.format(result[name]['per_avg']))


print('전체 국어 평균점수는?')
avg_kor = 0
for name in result:
	avg_kor += int(result[name]['ko_score'])
avg_kor /= 3
print("전체 국어 평균 점수는 {}점.".format(avg_kor))
 
print('전체 영어 평균점수는?')
avg_eng = 0
for name in result:
	avg_eng += int(result[name]['en_score'])
avg_eng /= 3
print("전체 영어 평균 점수는 {}점.".format(avg_eng))
 
print('전체 수학 평균점수는?')
avg_math = 0
for name in result:
	avg_math += int(result[name]['math_score'])
avg_math /= 3
print("전체 수학 평균 점수는 {}점.".format(avg_math))
