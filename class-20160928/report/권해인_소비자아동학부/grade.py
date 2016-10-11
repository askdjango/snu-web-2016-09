print('[2016 벤처창업웹프로그래밍1] 소비자아동학부, 권해인')
print()
result={}
for i in range(1,4):
	name = input('{}번째 학생 이름은? '.format(i))
	ko_score = input('{}님의 국어 시험 점수는?'.format(name))
	en_score = input('{}님의 영어 시험 점수는?'.format(name))
	math_score = input('{}님의 수학 시험 점수는?'.format(name))
	result[name] = {
		'ko_score': float(ko_score),
		'en_score': float(en_score),
		'math_score': float(math_score)
	}

import statistics
print()
print('개별 평균점수')
mean_i={}
for name in result:
        mean_i[name] = statistics.mean(result[name].values())
        print('이름: {} 평균: {}, 국어: {ko_score}, 영어: {en_score}, 수학: {math_score}'.format(name, mean_i[name],**result[name]))

print()
print('전체 과목별 평균점수')
score={}
for subject in result[name]:
        for name in result:
                if subject not in score:
                        score[subject]=[result[name][subject]]
                else:
                        score[subject]=score[subject]+[result[name][subject]]
mean={}
for subject in score:
        mean[subject]=statistics.mean(score[subject])

print('국어: {ko_score}, 영어: {en_score}, 수학: {math_score}'.format(**mean))
