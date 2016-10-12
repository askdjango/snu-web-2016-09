print("성적 계산기")
score = {}
number = int(input("몇 명의 성적을 입력하시겠습니까? "))
if number <= 0:
    print('\n학생이 없기때문에 프로그램을 종료합니다')
    exit()

for i in range(1,number+1):
    Id = input('{}번째 학생의 학번은? '.format(i))
    ko_score = int(input('{}님의 국어 시험 점수는? '.format(Id)))
    en_score = int(input('{}님의 영어 시험 점수는? '.format(Id)))
    ma_score = int(input('{}님의 수학 시험 점수는? '.format(Id)))
    score[Id] = {
        'ko_score':ko_score,
        'en_score':en_score,
        'ma_score':ma_score,
    }

ko_sum = 0
en_sum = 0
ma_sum = 0

for student in score:
    ko_sum += score[student]['ko_score']
    en_sum += score[student]['en_score']
    ma_sum += score[student]['ma_score']
ko_average = ko_sum/number
en_average = en_sum/number
ma_average = ma_sum/number



select = input('''
어떤 결과를 보시겠습니까?
1.과목별 평균    2.개인 성적 리스트    3.개인 성적 검색    4. 종료
입력: ''')
while select == '1':
    print('\n과목별 평균 점수')
    print('국어:{}'.format(ko_average))
    print('영어:{}'.format(en_average))
    print('수학:{}'.format(ma_average))
    select = input('''
어떤 결과를 보시겠습니까?
1.과목별 평균    2.개인 성적 리스트    3.개인 성적 검색    4. 종료
입력: ''')


while select != '1':
    if select == '2':
        print('')
        for name in score:
            average = (score[name]['ko_score']+score[name]['en_score']+score[name]['ma_score'])/3
            print('[학번:{}]  평균: {}   국어: {}, 영어: {}, 수학: {}'.format(name,
            average,
            score[name]['ko_score'],score[name]['en_score'],score[name]['ma_score']))
        select = input('''
어떤 결과를 보시겠습니까?
1.과목별 평균    2.개인 성적 리스트    3.개인 성적 검색    4. 종료
입력: ''')

    elif select == '3':
        name = input('검색하려는 사람의 학번을 입력해주세요: ')
        if name in score:
            average = (score[name]['ko_score']+score[name]['en_score']+score[name]['ma_score'])/3
            print('\n학번:',name)
            print('평균 점수:', average)
            print('국어 점수:', score[name]['ko_score'])
            print('영어 점수:', score[name]['en_score'])
            print('수학 점수:', score[name]['ma_score'])
        else:
            print('해당하는 학생이 없습니다')
        select = input('''
어떤 결과를 보시겠습니까?
1.과목별 평균    2.개인 성적 리스트    3.개인 성적 검색    4. 종료
입력: ''')
    elif select == '4':
        print('\n프로그램을 종료합니다')
        break
    else:
        select = input("""\n'1'(과목별 평균), '2'(개인 성적 리스트),
'3'(개인 성적 검색), '4'(종료)의 값을 입력해주세요
입력: """)
    while select == '1':
        print('\n과목별 평균 점수')
        print('국어:{}'.format(ko_average))
        print('영어:{}'.format(en_average))
        print('수학:{}'.format(ma_average))
        select = input('''
어떤 결과를 보시겠습니까?
1.과목별 평균    2.개인 성적 리스트    3.개인 성적 검색    4. 종료
입력: ''')




