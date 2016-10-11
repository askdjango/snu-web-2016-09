for i in range(1,10):
    stars = -abs(2 * i - 10) + 9
    blanks = abs(i - 5)

    #문자열 형식 지정자 사용
    formula = ''
    for _ in range(blanks):
        formula += '{0}'
    for _ in range(stars):
        formula += '{1}'
    print(formula.format(' ', '*'))