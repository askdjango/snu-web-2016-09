message = '노랑 빨강 녹색 파랑 노랑 빨강 노랑 빨강'
color = message.split()

word = input("어떤 단어 갯수를 원해?")

a = 0

for i in color :
    if i == word :
        a = a + 1
    else :
        a = a + 0

print(a)