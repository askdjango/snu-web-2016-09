result = {}
nm = []
sc = {}
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
    nm.append(name)

print('개별 평균점수')
for name in result:
    name1= input('이름을 입력하세요:  ')
    a = float(result[name1]['ko_score'])
    b = float(result[name1]['en_score'])
    c = float(result[name1]['math_score'])
    print('[{}] 국어: {}, 영어: {}, 수학: {}'.format(name1,result[name1]['ko_score'],result[name1]['en_score'],result[name1]['math_score']))
    print('average = {}'.format((a+b+c)/3))
    print('\n')
    sc[name1] = {'ko': a, 'en': b, 'math': c}


print('전체 국어 평균점수는? {}'.format((sc[nm[0]]['ko']+sc[nm[1]]['ko']+sc[nm[2]]['ko'])/3))  # TODO: 계산하세요.
print('전체 영어 평균점수는? {}'.format((sc[nm[0]]['en']+sc[nm[1]]['en']+sc[nm[2]]['en'])/3))  # TODO: 계산하세요
print('전체 수학 평균점수는? {}'.format((sc[nm[0]]['math']+sc[nm[1]]['math']+sc[nm[2]]['math'])/3))  # TODO: 계산하세요.