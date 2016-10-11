for i in range(1,10):
    if i <= 5:
        star = i*2-1
        space = 5-i
        print(" "*space + "*"*star + " "*space)
    else:
        space2 = i-5
        star2 = 9-space2*2
        print(" "*space2 + "*"*star2 + " "*space2)

print("감사합니다.")