print('다이아몬드 만들기!')
select = input('''어떤 다이아몬드를 만드시겠습니까?
1. 형식 지정자를 사용하지 않은 다이아몬드
2. 형식 지정자를 사용하여 만든 다이아몬드
3. 만들지 않겠다
입력: ''')
if select == '3':
    print('프로그램을 종료합니다')
    exit()

while select == '1':
    print('\n형식 지정자를 사용하지 않고 만드는 다이아몬드')
    size = int(input("몇층까지 넓어지는 다이아몬드를 만들까요?: "))
    floor = 1
    while floor < size:
        amount = floor*2 -1
        blank = size - floor
        print(' '*blank, end='')
        print('*'*amount)
        floor += 1
    while floor >= 1:
        amount = floor*2 -1
        blank = size - floor
        print(' '*blank, end ='')
        print('*'*amount)
        floor-= 1
    select = input('''
다시 다이아몬드를 만드시겠습니까?
1. 형식 지정자를 사용하지 않은 다이아몬드를 다시 만든다
2. 형식 지정자를 사용하여 만든 다이아몬드를 다시 만든다
3. 그만하겠다
입력: ''')

while select != '1':
    if select == '2':
        print('\n형식 지정자를 사용하여 만드는 다이아몬드')
        size = int(input("몇층까지 넓어지는 다이아몬드를 만들까요?: "))
        wide = '{:^' + str((size*2) - 1) + '}'
        floor = 1
        while floor < size:
            amount = floor*2 -1
            print(wide.format('*'*amount))
            floor += 1
        while floor >= 1:
            amount = floor*2 - 1
            print(wide.format('*'*amount))
            floor -= 1
        select = input('''다시 다이아몬드를 만드시겠습니까?
1. 형식 지정자를 사용하지 않은 다이아몬드를 다시 만든다
2. 형식 지정자를 사용하여 만든 다이아몬드를 다시 만든다
3. 그만하겠다
입력: ''')
    elif select == '3':
        print('''\n사실 1번이나 2번이나 출력값은 같다...
프로그램을 종료합니다''')
        break
    else:
        select = input("\n'1'(형식지정자 사용 x), '2'(형식지정자 사용),'3'(종료)의 값을 입력해주세요: ")
    while select == '1':
        print('\n형식 지정자를 사용하지 않고 만드는 다이아몬드')
        size = int(input("몇층까지 넓어지는 다이아몬드를 만들까요?: "))
        floor = 1
        while floor < size:
            amount = floor*2 -1
            blank = size - floor
            print(' '*blank, end='')
            print('*'*amount)
            floor += 1
        while floor >= 1:
            amount = floor*2 -1
            blank = size - floor
            print(' '*blank, end ='')
            print('*'*amount)
            floor-= 1
        select = input('''다시 다이아몬드를 만드시겠습니까?
1. 형식 지정자를 사용하지 않은 다이아몬드를 다시 만든다
2. 형식 지정자를 사용하여 만든 다이아몬드를 다시 만든다
3. 그만하겠다
입력: ''')



