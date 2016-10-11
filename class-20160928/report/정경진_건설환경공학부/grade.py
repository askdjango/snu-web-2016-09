result = {}
korean = 0
english = 0
math = 0

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
    korean += int(result[name]['ko_score'])
    english += int(result[name]['en_score'])
    math += int(result[name]['math_score'])
    # TODO: 구현하세요.
    print('[{}] 국어: {}, 영어: {}, 수학: {}'.format(name, result[name]['ko_score'], result[name]['en_score'], result[name]['math_score']))


print('전체 국어 평균점수는? {}'.format(korean / len(result)))  # TODO: 계산하세요.
print('전체 영어 평균점수는? {}'.format(english / len(result)))  # TODO: 계산하세요.
print('전체 수학 평균점수는? {}'.format(math / len(result)))  # TODO: 계산하세요.