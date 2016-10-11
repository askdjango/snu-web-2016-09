import decimal
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

print('-------------------')
print('개별 평균점수')
#print(result)
for (name, score) in result.items():
    nums1 = score.values()
    nums2 = list(map(int, nums1))
    aver = sum(nums2) / len(nums2)
    #aver2 = decimal.Decimal(aver1)
    print('{}: 평균 {}점 / 국어: {}점, 영어: {}점, 수학: {}점'  .format(name, round(aver,2), ko_score, en_score, math_score))

ko_total = []
en_total = []
math_total = []

for (name, score) in result.items():
    ko = score['ko_score']
    en = score['en_score']
    math = score['math_score']
    ko_total.append(ko)
    en_total.append(en)
    math_total.append(math)

ko_total2 = list(map(int, ko_total))
en_total2 = list(map(int, en_total))
math_total2 = list(map(int, math_total))

ko_aver = sum(ko_total2) / len(ko_total2)
en_aver = sum(en_total2) / len(en_total2)
math_aver = sum(math_total2) / len(math_total2)

print('전체 국어 평균점수는? {}점'.format(round(ko_aver,2)))  # TODO: 계산하세요.
print('전체 영어 평균점수는? {}점'.format(round(en_aver,2)))  # TODO: 계산하세요.
print('전체 수학 평균점수는? {}점'.format(round(math_aver,2)))  # TODO: 계산하세요.