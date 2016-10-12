word = '노랑 빨강 녹색 파랑 노랑 빨강 노랑 빨강'

word_list = word.split()

word_list_unre = list(set(word_list))
for i in range(0,len(word_list_unre)):
        print (word_list_unre[i],"의 갯수는 : ",word.count(word_list_unre[i]))
