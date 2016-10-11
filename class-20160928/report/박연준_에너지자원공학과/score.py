
result = {}

for i in range(1, 4):
    name = input('{} 번째 학생 이름은? '.format(i))
    ko_score = float(input('{}님의 국어 시험 점수는? '.format(name)))
    en_score = float(input('{}님의 영어 시험 점수는? '.format(name)))
    math_score = float(input('{}님의 수학 시험 점수는? '.format(name)))
    result[name] = {
        'ko_score': ko_score,
        'en_score': en_score,
        'math_score': math_score,
    }

print('개별 평균점수')
for name in result:
    a = result[name]['ko_score']
    b = result[name]['en_score']
    c = result[name]['math_score']
    average = (a + b + c) / 3
    print('[{}] 국어: {}, 영어: {}, 수학: {}, 평균점수 : {}'.format(name, a, b, c, average))

print('전체 국어 평균점수는?')
sum = 0
for name in result:
     sum += result[name]['ko_score']
ko_average = sum / 3
print(ko_average)
print('전체 영어 평균점수는?')
sum = 0
for name in result:
     sum += result[name]['en_score']
en_average = sum / 3
print(en_average)
print('전체 수학 평균점수는?')
sum = 0
for name in result:
     sum += result[name]['math_score']
math_average = sum / 3
print(math_average)
