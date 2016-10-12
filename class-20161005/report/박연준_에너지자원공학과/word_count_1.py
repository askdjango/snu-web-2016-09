'''
과제 2, 과제1에서는 input 값을 입력받아 count메서드를 써서 찾아 내었다.
그러나 원래 과제의 의미는 각 각 갯수가 몇 개 인지 담아서 출력하는 함수였다.
딕셔너리를 써서 key에 색깔, value에 없으면 1을 추가하고 있으면 1씩 더해가며 출력하는 코드로 해결하였다.
'''


message = '노랑 빨강 녹색 파랑 노랑 빨강 노랑 빨강'

result = {}

for word in message.split():
    if word in result:
        result[word] += 1
    else:
        result[word] = 1

print(result)
