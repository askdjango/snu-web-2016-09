for i in range(1,10):
    stars = -abs(2 * i - 10) + 9
    blanks = abs(i - 5)
    print(' ' * blanks + '*' * stars)