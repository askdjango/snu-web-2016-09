# 3. 단어 횟수 카운트
color_list = ['red', 'green', 'blue', 'blue', 'green', 'black', 'black', 'lime']
colors = ','.join(color_list)

print('색깔 리스트: {}'.format(colors))
selected_color = input("색깔 리스트 중에서 색깔을 하나 골라서 입력해 주세요: ")

count = 0
for color in color_list:
    if color == selected_color:
        count += 1

print('{}은/는 {}개 있습니다.'.format(selected_color, count))
