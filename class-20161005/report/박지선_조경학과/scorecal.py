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

ko_ss = 0
en_ss = 0
math_ss = 0

print('개별 평균점수')
for name in result:
    result[name]
    average=(int(result[name]['ko_score'])+int(result[name]['en_score'])+int(result[name]['math_score']))/3
    total = result[name]['ko_score'] + result[name]['en_score'] + result[name]['math_score']

    print('[{}] 국어 : {} , 수학 : {} , 영어 : {}, 평균 : {}'.format(name, result[name]['ko_score'],result[name]['en_score'],result[name]['math_score'],average))

for name in result:

    ko_ss += int(result[name]['ko_score'])
    en_ss += int(result[name]['en_score'])
    math_ss +=int(result[name]['math_score'])


ko_ss = ko_ss/3
en_ss = en_ss/3
math_ss = math_ss/3


print('전체 평균점수: 국어{}점, 영어{}점, 수학{}점'.format(ko_ss,en_ss,math_ss))
