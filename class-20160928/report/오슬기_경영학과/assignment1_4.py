message = input('색깔을 한 칸씩 띄어쓰기 하여 입력해주세요.')
color = message.split()
print(color)

word = input("갯수를 알고 싶은 색깔 : ")
count = color.count(word)
print(count)