message = '노랑 빨강 녹색 파랑 노랑 빨강 노랑 빨강'
splitedMessage = message.split()
while True:
    wanted = input('노랑,빨강,초록,파랑 중에 하나를 입력해주세요!\n')
    if wanted == 'stop':
        break
    elif wanted == '노랑'or'빨강'or'초록'or'파랑':
        print(splitedMessage.count(wanted))
    else:
        print('잘못된 입력입니다.'')
