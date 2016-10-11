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

summ = {}
avg = {}

print('개별 평균점수')

for name in result:
    summ[name] = result[name]['ko_score']+result[name]['en_score']+result[name]['math_score']
    avg[name] = float(summ[name] / 3)

    # TODO: 구현하세요.
    print('{}님의 평균점수 : [{}]'.format(name, avg[name]))
    print('국어: {ko_score}, 영어: {en_score}, 수학: {math_score}'.format(**result[name]))



print('전체 국어 평균점수는?')  # TODO: 계산하세요.

ko_summ_all = 0

for name in result :
    ko_summ_all = ko_summ_all + result[name]['ko_score']

ko_avg_all = float(ko_summ_all / 3 )
print(ko_avg_all)

print('전체 영어 평균점수는?')  # TODO: 계산하세요.

en_summ_all = 0

for name in result :
    en_summ_all = en_summ_all + result[name]['en_score']

en_avg_all = float(en_summ_all / 3 )
print(en_avg_all)

print('전체 수학 평균점수는?')  # TODO: 계산하세요.

math_summ_all = 0

for name in result :
    math_summ_all = math_summ_all + result[name]['math_score']

math_avg_all = float(math_summ_all / 3 )
print(math_avg_all)
