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
    result[name]
    print('[{' + name + '}] 국어: {' + result[name]['ko_score'] + '}, 영어: {' + result[name]['en_score'] + '}, 수학: {' + result[name]['math_score'] + '}')


ko_total_score = 0
en_total_score = 0
math_total_score = 0

for name in result:
    result[name]
    ko_total_score += int(result[name]['ko_score'])
    en_total_score +=int(result[name]['en_score'])
    math_total_score +=int(result[name]['math_score'])

ko_total_score = ko_total_score/3
en_total_score = en_total_score/3
math_total_score = math_total_score/3


print('전체 국어 평균 점수는? ',ko_total_score)
print('전체 영어 평균 점수는? ',en_total_score)
print('전체 수학 평균 점수는? ', math_total_score)

