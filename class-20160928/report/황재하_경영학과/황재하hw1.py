#구구단 출력 프로그램
number = int(input("구구단으로 계산해 볼 숫자를 입력하세요:"))
for i in range(1,10):
    print(number, 'x', i, '=', number*i)
print('\nEnter를 눌러누세요')
input()

#다이아몬드 만들기 1
print('''
형식 지정자를 사용하지 않은 다이아몬드
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *     ''')

#다이아몬드 만들기 2
print('\n형식 지정자를 사용한 다이아몬드')
print('''{0}
{1}
{2}
{3}
{4}
{3}
{2}
{1}
{0}'''
.format('    *','   ***','  *****',' *******','*********'))

print('\nEnter를 눌러누세요')
input()

#한 문자열에서 지정 단어의 횟수를 카운트
print('\n한 문자열에서 지정 단어의 횟수를 카운트')
message = '노랑 빨강 녹색 파랑 노랑 빨강 노랑 빨강'
checker = list(message.split())
print(checker)
red = 0
yellow = 0
blue = 0
green = 0
for k in range(0,8):
    if checker[k] == '빨강':
        red += 1
    elif checker[k] == '노랑':
        yellow +=1
    elif checker[k] == '녹색':
        green += 1
    else:
        blue += 1
print('빨강의 개수는', red,
      '\n노랑의 개수는', yellow,
      '\n녹색의 개수는', green,
      '\n파랑의 개수는', blue)

print('\nEnter를 눌러누세요')
input()

#성적 계산기
print('\n성적 계산기')
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


kosum = 0
ensum = 0
masum = 0
print('개별 평균점수')
for name in result:
    result[name]
    kosum = kosum + int(result[name]['ko_score'])
    ensum = ensum + int(result[name]['en_score'])
    masum = masum + int(result[name]['math_score'])
    total = 0
    value = list(result[name].values())
    score = map(int,value)
    for s in score:
        total = total + s
        average = total/3
    print('[{}]  평균: {} 국어: {}, 영어: {}, 수학: {}'.format(name,
        average,
        result[name]['ko_score'],result[name]['en_score'],result[name]['math_score']))




print('전체 국어 평균점수는?', kosum/3)  # TODO: 계산하세요.
print('전체 영어 평균점수는?', ensum/3)  # TODO: 계산하세요.
print('전체 수학 평균점수는?', masum/3)  # TODO: 계산하세요.



