from itertools import count

message = "노랑 빨강 녹색 파랑 노랑 빨강 노랑 빨강"
word_list = message.split()
word_index = list(set(word_list))

for i in range(len(word_index)):
    word = word_index[i]
    count = word_list.count(word)
    print('{} : {}개'.format(word,count))