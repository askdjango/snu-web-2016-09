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

total_ko = 0
total_en = 0
total_math = 0

print('개별 평균점수')
for name in result:
    ko_score = int(result[name]['ko_score'])
    en_score = int(result[name]['en_score'])
    math_score = int(result[name]['math_score'])
    print('[{}] 국어: {}, 영어: {}, 수학: {}'.format(name,ko_score,en_score,math_score))

    total_ko += ko_score
    total_en += en_score
    total_math += math_score

print('전체 국어 평균점수는? {}'.format(total_ko/len(result)))
print('전체 영어 평균점수는? {}'.format(total_en/len(result)))
print('전체 수학 평균점수는? {}'.format(total_math/len(result)))
