word_list=['노랑', '빨강', '녹색', '파랑', '노랑', '빨강', '노랑', '빨강']
yellow = 0
red = 0
green = 0
blue = 0
for i in word_list:
    if i == '노랑':
        yellow += 1
    elif i == '빨강':
        red += 1
    elif i == '녹색':
        green += 1
    elif i == '파랑':
        blue += 1

print('노랑: %d, 빨강: %d, 녹색: %d, 파랑: %d' %(yellow, red, green, blue))