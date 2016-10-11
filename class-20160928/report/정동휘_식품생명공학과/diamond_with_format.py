number = [1,3,5,7,9,7,5,3,1]
for i in range(9):
    stars = str('*'*number[i])
    print(format(stars, '^40'))