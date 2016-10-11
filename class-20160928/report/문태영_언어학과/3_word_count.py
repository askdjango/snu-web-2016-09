
#한 문자열에서 지정 단어의 횟수를 카운트하는 프로그램을 작성
print("\n# 한 문자열에서 지정 단어의 횟수를 카운트하는 프로그램")
print("\n    (1) 직접 문자열을 입력하기")
print("    (2) default 값으로 진행하기")
print("        (default 값 : '노랑 빨강 녹색 파랑 노랑 빨강 노랑 빨강')")
menu = int(input("\n원하시는 메뉴 번호를 입력하세요 : "))
while menu<1 or menu>2:
    menu = int(input("유효한 메뉴 번호를 입력하세요 : "))

if menu == 1:
    message = str(input("문자열을 입력해주세요 : "))

if menu == 2:
    message = "노랑 빨강 녹색 파랑 노랑 빨강 노랑 빨강"

li = message.split()
dic = {}

for i in li:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

print("\n    (1) 모든 단어의 횟수 확인하기")
print("    (2) 특정 단어의 횟수 확인하기")

menu = int(input("\n원하시는 메뉴 번호를 입력하세요 : "))
while menu<1 or menu>2:
    menu = int(input("유효한 메뉴 번호를 입력하세요 : "))

if menu == 1:
    print(dic)

if menu == 2:
    word_list = []

    for i in dic:
        word_list.append(i)
    print("\n")
    print(word_list)

    target_word = str(input("위의 리스트 안의 단어들 중 확인하려는 단어를 입력하세요 : "))

    while target_word not in word_list:
        target_word = str(input("\n입력하신 단어가 리스트 안에 존재하지 않습니다.\n위의 리스트 안의 단어들 중 확인하려는 단어를 입력하세요 : "))

    print("'"+target_word+"' : "+str(dic[target_word]))


