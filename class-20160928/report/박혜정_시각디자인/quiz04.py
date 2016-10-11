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
    ko = result[name]['ko_score']
    en = result[name]['en_score']
    math = result[name]['math_score']
    person_average = (int(ko) + int(en) + int(math)) / 3
    print('[{}] 국어: {}, 영어: {}, 수학: {}'.format(person_average, ko, en, math))

print('전체 국어 평균점수는?')
ko_sum = 0
for name in result:
    ko_sum += int(result[name]['ko_score'])
print(ko_sum / 3)

print('전체 영어 평균점수는?')
en_sum = 0
for name in result:
    en_sum += int(result[name]['en_score'])
print(en_sum / 3)

print('전체 수학 평균점수는?')
math_sum = 0
for name in result:
    math_sum += int(result[name]['math_score'])
print(math_sum / 3)