lst = '노랑 빨강 노랑 초록 파랑 초록 빨강 노랑 초록 파랑 빨강 빨강 노랑 노랑 노랑 초록 노랑 '

splited_lst = lst.split()

print( '목록', '<', lst, '>' )

print('''

        ''')


color = str(input(' 노랑, 빨강, 초록, 파랑 중 하나를 입력하시오. '))

print('''

        ''')

if color is '노랑' or '빨강' or '초록' or '파랑' :



    print( '선택하신 색은 %d 개 입니다. ' % splited_lst.count(color) )




else :
    print ( '색을 잘못 입력하셨습니다. 다시 시도해주세요. ')

print('''

        ''')