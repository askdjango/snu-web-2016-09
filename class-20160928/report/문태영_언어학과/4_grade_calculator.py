
#성적 계산 프로그램 완성하기

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

print('\n개별 평균점수')
for name in result:
    dic = result[name]
    sum = 0
    for i in dic:
        sum += float(dic[i])
    avrg_score = sum/len(dic)
    dic['average']=avrg_score
    print('[{}] 평균점수 : {:.2f}점, 국어: {}점, 영어: {}점, 수학: {}점'.format(name, dic['average'], dic['ko_score'], dic['en_score'], dic['math_score'] ))


print('\n전체 국어 평균점수는?')
sum = 0
for name in result:
    sum += float(result[name]['ko_score'])
print('{:.2f}점'.format(sum/len(result)))

print('전체 영어 평균점수는?')
sum = 0
for name in result:
    sum += float(result[name]['en_score'])
print('{:.2f}점'.format(sum/len(result)))

print('전체 수학 평균점수는?')
sum = 0
for name in result:
    sum += float(result[name]['math_score'])
print('{:.2f}점'.format(sum/len(result)))

