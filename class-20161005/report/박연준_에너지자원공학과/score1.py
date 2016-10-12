# 과제 2에서는 함수로 표현해 보았다.

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

def average_score(key, kwargs):
    sum = 0
    for name in kwargs:
        sum += kwargs[name][key]

    return sum / len(kwargs)


print('개별 평균점수')
for name in result:
    a = result[name]['ko_score']
    b = result[name]['en_score']
    c = result[name]['math_score']
    average = (a + b + c) / len(result[name])
    print('[{}] 국어: {}, 영어: {}, 수학: {}, 평균점수 : {}'.format(name, a, b, c, average))

print('전체 국어 평균점수는?')
ko_average = average_score('ko_score', result)
print(ko_average)

print('전체 영어 평균점수는?')
en_average = average_score('en_score', result)
print(en_average)

print('전체 수학 평균점수는?')
math_average = average_score('math_score', result)
print(math_average)
