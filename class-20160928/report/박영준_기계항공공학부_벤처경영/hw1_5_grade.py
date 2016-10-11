
result = {}
num = 3

for i in range(1, 1+num):
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
    dict = result[name]
    # TODO: 구현하세요.
    mean=int((dict['ko_score']+dict['en_score']+dict['math_score'])/3)
    print('[{}] 국어: {}, 영어: {}, 수학: {}'.format(mean,dict['ko_score'],dict['en_score'],dict['math_score']))

ko_sum=0
en_sum=0
math_sum=0

for key in result:
    ko_sum += result[key]['ko_score']
    en_sum += result[key]['en_score']
    math_sum += result[key]['math_score']

print('전체 국어 평균점수는?')  # TODO: 계산하세요.
print(ko_sum/num)
print('전체 영어 평균점수는?')  # TODO: 계산하세요.
print(en_sum/num)
print('전체 수학 평균점수는?')  # TODO: 계산하세요.
print(math_sum/num)