result = {}
ko_sum = 0
en_sum = 0
math_sum = 0

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
    print('%s님 국어: %d, 영어: %d, 수학: %d' %(name, int(result[name]['ko_score']), int(result[name]['en_score']), int(result[name]['math_score'])))
    ko_sum += int(result[name]['ko_score'])
    en_sum += int(result[name]['en_score'])
    math_sum += int(result[name]['math_score'])
    # TODO: 구현하세요.

ko_avr = ko_sum/3.0
en_avr = en_sum/3.0
math_avr = math_sum/3.0
print('전체 국어 평균점수는? %f' %(ko_avr))  # TODO: 계산하세요.
print('전체 영어 평균점수는? %f' %en_avr)  # TODO: 계산하세요.
print('전체 수학 평균점수는? %f' %math_avr)  # TODO: 계산하세요.