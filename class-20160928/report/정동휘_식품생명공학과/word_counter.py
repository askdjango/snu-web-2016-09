message = '노랑 빨강 녹색 파랑 노랑 빨강 노랑 빨강'
print('문자열: '+message)
word_list = message.split()
yellow_count = 0
red_count = 0
blue_count = 0
green_count = 0

for i in range(len(word_list)):
    if '노랑' == word_list[i]:
        yellow_count = yellow_count + 1
    elif '빨강' == word_list[i]:
        red_count = red_count + 1
    elif '파랑' == word_list[i]:
        blue_count = blue_count + 1
    elif '녹색' == word_list[i]:
        green_count = green_count + 1
print("문자열에서 각 색상의 개수는 노랑: {yellow_count}개, 빨강: {red_count}개, 파랑: {blue_count}개, 녹색: {green_count}개 입니다.".format(yellow_count = str(yellow_count), red_count = str(red_count), blue_count = str(blue_count), green_count = str(green_count)))