#2. 다이아몬드 그리기

def draw_diamond(number):
    space = [(' '*i) for i in range(number)]
    star = [('*'*int(2*i-1)) for i in range(1,number+1)]
    result = ['{}{}'.format(space[::-1][num], star[num]) for num in range(len(space))]

    new_result = result[:number-1] + result[::-1]
    print('\n'.join(new_result))

draw_diamond(7)
