size = int(input("원하는 다이아의 크기(홀수)를 입력하세요."))


print ( '''


        ''')

if size % 2 == 0 :
    print (" 홀수만 입력하실 수 있습니다. ")


else :
    half_size = int ( (1+size)/2 )

    for i in range (1, half_size + 1) :
        blank = half_size - i
        star = 2*i - 1

        print ( '{}{}' .format(' ' * blank , '*' * star)  )

    for i in range ( half_size + 1, size + 1 ) :
        blank = half_size + i - size - 1
        star = 2*size - 2*i + 1

        print ( '{}{}' .format(' ' * blank , '*' * star) )

    print ( ' 크기 %d 의 다이아가 완성되었습니다. ' % size )
    print ( '''


        ''')