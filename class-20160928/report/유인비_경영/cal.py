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

total_ko = total_en = total_math = 0

for name in result:
    print('[{}] 국어: {}, 영어: {}, 수학: {}'. format(name, result[name]['ko_score'], result[name]['en_score'], result[name]['math_score']))
    total_ko = total_ko + int(result[name]['ko_score'])
    total_en = total_en + int(result[name]['en_score'])
    total_math = total_math + int(result[name]['math_score'])

average_ko = total_ko / 3
average_en = total_en / 3
average_math = total_math / 3


print('전체 국어 평균점수는? : %d' % average_ko)  # TODO: 계산하세요.
print('전체 영어 평균점수는? : %d' % average_en)  # TODO: 계산하세요.
print('전체 수학 평균점수는? : %d' % average_math)  # TODO: 계산하세요.

print('감사합니다.')