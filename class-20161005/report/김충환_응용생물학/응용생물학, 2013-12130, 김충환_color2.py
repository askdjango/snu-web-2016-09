word_list = ['노랑', '빨강', '녹색', '파랑', '노랑', '빨강', '노랑', '빨강']

y = 0
r = 0
g = 0
b = 0

for i in word_list :
    if i =='노랑':
        y += 1

    elif i =='빨강' : 
        r += 1

    elif i =='녹색' :
        g += 1

    else :
        b +=1

print('노랑 :', y, '빨강 :', r, '녹색 : ', g, '파랑 : ', b)
