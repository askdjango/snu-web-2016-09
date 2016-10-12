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

print('-------------------')
print('개별 평균점수')
#print(result)
for name in result:
    total = result[name]['ko_score'] + result[name]['en_score'] + result[name]['math_score']
    average = total / 3
    print('{}: 평균 {}점 / 국어: {}점, 영어: {}점, 수학: {}점' .format(name, round(average, 2), result[name]['ko_score'], result[name]['en_score'], result[name]['math_score']))


ko_total = 0
for name in result:
    ko_total += result[name]['ko_score']
ko_average = ko_total / len(result)
print('전체 국어 평균점수는? {}점'.format(round(ko_average,2)))

en_total = 0
for name in result:
    en_total += result[name]['en_score']
en_average = en_total / len(result)
print('전체 영어 평균점수는? {}점'.format(round(en_average,2)))

math_total = 0
for name in result:
    math_total += result[name]['math_score']
math_average = math_total / len(result)
print('전체 수학 평균점수는? {}점'.format(round(math_average,2)))