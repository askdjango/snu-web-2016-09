word_list = ['노랑', '빨강', '녹색', '파랑', '노랑', '빨강', '노랑', '빨강']
h = 0
j = 0
k = 0
l=0
for i in range(7):
    if '노랑' in word_list[i]:
        h +=1
    elif '빨강' in word_list[i]:
        j +=1
    elif '녹색' in word_list[i]:
        k +=1
    elif '파랑' in word_list[i]:
        l +=1

print('노랑 : {}, 빨강 : {}, 녹색 : {}, 파랑 : {}'.format(h,j,k,l))