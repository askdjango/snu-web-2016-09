word_list = ['노랑', '빨강', '녹색', '파랑', '노랑', '빨강', '노랑', '빨강']
word_set = list(set(word_list))
word_set_number = int(len(word_set))
word_list_number = int(len(word_list))
for j in range (0,word_set_number):
	a = 0
	for i in range (0,word_list_number):
		if word_set[j] == word_list[i]:
			a+=1
	print(word_set[j],':',a)

