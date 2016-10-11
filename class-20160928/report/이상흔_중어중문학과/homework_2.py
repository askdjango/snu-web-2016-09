#2. 다이아몬드 그리기

#2-1. 형식 지정자 사용
space = [(' '*i) for i in range(5)]
star = [('*'*int(2*i-1)) for i in range(1,6)]
result = ['{}{}'.format(space[::-1][num], star[num]) for num in range(len(space))]

new_result = result[:4] + result[::-1]
print('\n'.join(new_result))

#2-2. 형식 지정자 미사용
space = [(' '*i) for i in range(5)]
star = [('*'*int(2*i-1)) for i in range(1,6)]
result = [(space[::-1][num] + star[num]) for num in range(len(space))]

new_result = result[:4] + result[::-1]
print('\n'.join(new_result))
