# 3. 단어 횟수 카운트

def show_list():
    color_list = ['red', 'green', 'blue', 'blue', 'green', 'black', 'black', 'lime']
    colors = ','.join(color_list)
    print('색깔 리스트: {}'.format(colors))
    return color_list

def color_input():
    selected_color = input("색깔 리스트 중에서 색깔을 하나 골라서 입력해 주세요: ")
    return selected_color

def count_color():
    count = 0
    for color in color_list:
        if color == selected_color:
            count += 1
    return count

def print_result():
    print('{}은/는 {}개 있습니다.'.format(selected_color, count))

color_list = show_list()
selected_color = color_input()
count = count_color()
print_result()
