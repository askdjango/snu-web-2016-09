# 1. 구구단

def print_99dan(num):
    if num < 10:
        for i in range(1,10):
            result = '{} x {} = {}'.format(num, i, i*num)
            print(result)
    else:
        print("9 이하의 숫자를 입력하셔야 합니다.")

print_99dan(2)
