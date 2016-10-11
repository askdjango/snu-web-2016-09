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
total_ko_score=0
total_en_score=0
total_math_score=0


print('개별 평균점수')
for name in result:
    print('[{}의 평균점수:{}] 국어: {}, 영어: {}, 수학: {}'.format(
        name,
        (int(result[name]['ko_score'])+int(result[name]['en_score'])+int(result[name]['math_score']))/3,
        result[name]['ko_score'],
        result[name]['en_score'],
        result[name]['math_score'])
    )
    total_ko_score+=int(result[name]['ko_score'])
    total_en_score+=int(result[name]['en_score'])
    total_math_score+=int(result[name]['math_score'])
print('전체 국어 평균점수는?',total_ko_score/3)  # TODO: 계산하세요.
print('전체 영어 평균점수는?',total_en_score/3)  # TODO: 계산하세요.
print('전체 수학 평균점수는?',total_math_score/3)  # TODO: 계산하세요.
