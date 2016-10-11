# 1. 구구단
num = int(input("숫자를 입력해 주세요 "))
if num < 10:
    for i in range(1,10):
        result = '{} x {} = {}'.format(num, i, i*num)
        print(result)
else:
    print("9 이하의 숫자를 입력하셔야 합니다.")
