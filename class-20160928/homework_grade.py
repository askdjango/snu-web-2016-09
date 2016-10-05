
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

    print('[{}] 국어: {}, 영어: {}, 수학: {}, 평균: {}'.format(
        name, result[name]['ko_score'], result[name]['en_score'],
        result[name]['math_score'], average,
    ))


print('전체 국어 평균점수는?')  # TODO: 계산하세요.
ko_total = 0
for name in result:
    ko_total += result[name]['ko_score']
ko_average = ko_total / len(result)
print(ko_average)

print('전체 영어 평균점수는?')  # TODO: 계산하세요.
print('전체 수학 평균점수는?')  # TODO: 계산하세요.








