# 특정 수를 입력받아서, 구구단을 출력하는 프로그램을 작성
# 2번째 과제에서 수정할 부분이 없었습니다.

number = int(input("구구단 숫자를 입력하시오.\n"))
print("\n{} 구구단\n".format(number))

for i in range(1, 10):
    answer = number * i
    print("{} x {} = {}".format(number, i, answer))
