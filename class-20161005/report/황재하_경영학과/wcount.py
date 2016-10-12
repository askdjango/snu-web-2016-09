print('문장 내 단어 갯수 계산기')
message = input('단어의 갯수를 확인할 문장을 입력하세요: ')
counter = {}
for word in message.split():
    if word in counter:
        counter[word] +=1
    else:
        counter[word] = 1
total = 0
for count in counter:
    total += int(counter[count])


select = input('''
어떤 결과를 보시겠습니까?
1. 전체 결과      2. 개별 단어 검색      3. 종료: ''')
while select == '1':
    print('전체 단어의 갯수:',total)
    for word in counter:
        print("단어","'",word,"'",'의 갯수:',counter[word])
    select = input('''
어떤 결과를 보시겠습니까?
1. 전체 결과      2. 개별 단어 검색      3. 종료: ''')

while select != '1':
    if select =='2':
        checker = input("찾으시는 단어를 입력하세요: ")
        if checker in counter:
            print('해당 단어의 갯수:',counter[checker],)
        else:
            print('해당하는 단어가 없습니다')
        select = input('''
어떤 결과를 보시겠습니까?
1. 전체 결과      2. 개별 단어 검색      3. 종료: ''')
    elif select == '3':
        print('계산을 종료합니다')
        break
    else:
        select = input("'1'(전체 결과) 혹은 '2'(개별 단어 검색) 혹은 '3'(종료)의 값을 입력해주세요: ")
    while select == '1':#재설정 값이 1이 었을때
        print('전체 단어의 갯수:',total)
        for word in counter:#전체 갯수 공개
            print("단어","'",word,"'",'의 갯수:',counter[word])
        select = input('''
어떤 결과를 보시겠습니까?
1. 전체 결과      2. 개별 단어 검색      3. 종료: ''')
