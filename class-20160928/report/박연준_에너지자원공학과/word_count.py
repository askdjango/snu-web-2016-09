# 리스트에서 지정 단어 횟수를 카운트하는 프로그램 작섬

word_list = ['노랑', '빨강', '녹색', '파랑', '노랑', '빨강', '노랑', '빨강']

print("입력한 문자열 리스트")
print(word_list)

find_word = input("찾고 싶은 색깔을 적어주시오.(노랑, 빨강, 녹색, 파랑 중 하나)\n")

print("입력하신 {} 색깔은 총 {}개가 있습니다.".format(find_word, word_list.count(find_word)))
