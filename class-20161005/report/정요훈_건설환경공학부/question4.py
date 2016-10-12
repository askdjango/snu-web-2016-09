# Previous code
'''
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

print('개별 시험 점수')
for name in result:
    result[name]

    print('[{}] 국어: {}, 영어: {}, 수학: {}'.format(name, result[name]['ko_score'], result[name]['en_score'], result[name]['math_score']))

ko_sum = 0
ko_score_avg = 0
en_sum = 0
en_score_avg = 0
math_sum = 0
math_score_avg = 0

for name in result:
    ko_sum = ko_sum + int(result[name]['ko_score'])
    en_sum = en_sum + int(result[name]['en_score'])
    math_sum = math_sum + int(result[name]['math_score'])

ko_score_avg = ko_sum / 3
en_score_avg = en_sum / 3
math_score_avg = math_sum / 3

print('전체 국어 평균점수는? [{}]'.format(ko_score_avg))

print('전체 영어 평균점수는? [{}]'.format(en_score_avg))

print('전체 수학 평균점수는? [{}]'.format(math_score_avg))
'''

# Revised code

result = {}

for i in range(1, 4):
    name = input('{} 번째 학생 이름은? '.format(i))
    ko_score = int(input('{}님의 국어 시험 점수는? '.format(name)))
    en_score = int(input('{}님의 영어 시험 점수는? '.format(name)))
    math_score = int(input('{}님의 수학 시험 점수는? '.format(name)))
    result[name] = {
        'ko_score': ko_score,
        'en_score': en_score,
        'math_score': math_score,
    }

print('개별 평균점수')
for name in result:
    total = result[name]['ko_score'] + result[name]['en_score'] + result[name]['math_score']
    average = total / 3

# Adding 개인 평균점수
    print('[{}] 국어: {}, 영어: {}, 수학: {}, 평균: {}'.format(
        name, result[name]['ko_score'], result[name]['en_score'],
        result[name]['math_score'], average,
    ))

print('전체 국어 평균점수는?')
ko_total = 0
for name in result:
    ko_total += result[name]['ko_score']
ko_average = ko_total / len(result)
print(ko_average)

print('전체 영어 평균점수는?')
en_total = 0
for name in result:
    en_total += result[name]['en_score']
en_average = en_total / len(result)
print(en_average)

print('전체 수학 평균점수는?')
math_total = 0
for name in result:
    math_total += result[name]['math_score']
math_average = math_total / len(result)
print(math_average)

