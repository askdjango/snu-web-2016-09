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
ko_total = 0
en_total = 0
math_total = 0

print('개별 점수 & 평균점수')
for name in result:
    ko_total = ko_total + int(result[name]['ko_score'])
    en_total = en_total + int(result[name]['en_score'])
    math_total = math_total + int(result[name]['math_score'])
    person_avg = (int(result[name]['ko_score']) + int(result[name]['en_score']) + int(result[name]['math_score'])) / 3
    print('[{}] 국어: {}, 영어: {}, 수학: {}, 평균 점수: {}'.format(name,str(result[name]['ko_score']),str(result[name]['en_score']),str(result[name]['math_score']),str(person_avg)))

ko_avg = ko_total / 3
en_avg = en_total / 3
math_avg = math_total / 3

print('전체 국어 평균점수는? '+str(ko_avg))
print('전체 영어 평균점수는? '+str(en_avg))
print('전체 수학 평균점수는? '+str(math_avg))
