size = int(input("원하는 다이아몬드의 크기는?"))



for i in range ( 1, size + 1 ) :
    blank = size - i
    star = 2 * i - 1

    print ( ' {}{} ' .format( ' ' * blank , '*' * star )   )

for i in range ( size + 1, size * 2 ) :
    blank = i - size
    star = size * 4 - 2 * i - 1

    print ( ' {}{} ' .format( ' ' * blank , '*' * star ) )

print ( ' %d 다이아 완성^^ ' % size )