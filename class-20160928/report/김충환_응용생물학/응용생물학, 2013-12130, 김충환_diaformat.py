for i in range(1,6) :
    blank = ' '*abs(5-i)
    star = '*'*(2*i-1)
    print('{}{}{}'.format(blank,star,blank))
for i in range(6,10) :
    blank = ' '*abs(5-i)
    star = '*'*(19-2*i)
    print('{}{}{}'.format(blank,star,blank))
