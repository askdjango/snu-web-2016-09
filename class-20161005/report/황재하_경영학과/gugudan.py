number = int(input("구구단으로 계산해볼 숫자를 입력해주세요: "))
for g in range(1,10):
    print(number,'x',g,'=',number*g)
retry = input("다시 해볼까요?(yes/no): ")
while retry != 'no':
    if retry == 'yes':
        number = int(input("구구단으로 계산해볼 숫자를 입력해주세요: "))
        for g in range(1,10):
            print(number,'x',g,'=',number*g)
        retry = input("다시 해볼까요?(yes/no): ")
    else:
        retry = input("'yes' 혹은 'no'으로 입력해주세요: ")
print("계산을 종료합니다")

