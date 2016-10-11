print('과제 1-4번을 시작합니다.')
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

ko_sum=0
en_sum=0
math_sum=0

print('개별 평균점수')
for name in result:
    scores=result[name]
    mean=(scores['ko_score']+scores['en_score']+scores['math_score'])/3
    print('[{}]님의 평균점수는{}입니다. 국어: {}, 영어: {}, 수학: {}'.format(name,mean,scores['ko_score'],scores['en_score'],scores['math_score']))

    ko_sum=ko_sum+scores['ko_score']
    en_sum=en_sum+scores['en_score']
    math_sum=math_sum+scores['math_score']


print('전체 국어 평균점수는?')
print(ko_sum/3) # TODO: 계산하세요.
print('전체 영어 평균점수는?')
print(en_sum/3)  # TODO: 계산하세요.
print('전체 수학 평균점수는?') 
print(math_sum/3) # TODO: 계산하세요.