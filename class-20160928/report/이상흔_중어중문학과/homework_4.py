#4. 평균 계산하기

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
    ko_score = result[name]['ko_score']
    en_score = result[name]['en_score']
    math_score = result[name]['math_score']
    score = ko_score, en_score, math_score,
    avg = sum(score) / len(result)
    # TODO: 구현하세요.
    print('[{}] 국어: {}, 영어: {}, 수학: {}'.format(name, *score))
    print('평균 점수: {}'.format(avg))

print('전체 국어 평균점수는?')  # TODO: 계산하세요.
ko_avg_score = 0
for name in result:
    ko_avg_score += result[name]['ko_score'] / len(result)
print(ko_avg_score)
print('-'*50)

print('전체 영어 평균점수는?')  # TODO: 계산하세요.
en_avg_score = 0
for name in result:
    en_avg_score += result[name]['en_score'] / len(result)
print(en_avg_score)
print('-'*50)

print('전체 수학 평균점수는?')  # TODO: 계산하세요.
math_avg_score = 0
for name in result:
    math_avg_score += result[name]['math_score'] / len(result)
print(math_avg_score)


# result = {
#     'sang': {
#     'ko_score': 100,
#     'en_score': 90,
#     'math_score': 80
#     },
#     'heun': {
#     'ko_score': 100,
#     'en_score': 90,
#     'math_score': 80
#     },
#     'lee': {
#     'ko_score': 100,
#     'en_score': 90,
#     'math_score': 80
#     }
# }
