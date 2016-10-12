for i in range(1,10):
    if i<= 5:
        bl=' '*(6-i)
        st='*'*(i*2-1)
        print('{}{}{}'.format(bl,st,bl))

    else:
        bl=' '*(i-4)
        st='*'*(19-2*i)
        print('{}{}{}'.format(bl,st,bl))
