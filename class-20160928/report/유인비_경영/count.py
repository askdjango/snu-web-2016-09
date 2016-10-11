c=0
message = '노랑 빨강 녹색 파랑 노랑 빨강 노랑 빨강'
print(message.split())
color=input("원하는 색깔 : ")
for i in range(0,8):
    if message.split(' ')[i] == color:
        c += 1
print("원하는 색깔은 %d번 나온다." % c)

print("감사합니다.")