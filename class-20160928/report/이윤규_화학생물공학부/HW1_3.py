#과제 3번.
print('과제 3번을 시작합니다.')
count=0
colors ='노랑 빨강 녹색 파랑 노랑 빨강 노랑 빨강'
print('색깔 목록=',colors)
message=colors.split()
find=input('세고 싶은 색깔은 무엇입니까? : ')
for i in range(0,len(message)):
   if find==message[i]:
   	   count=count+1
print('당신이 원하는',find,'의 개수는',count,'입니다.' )
