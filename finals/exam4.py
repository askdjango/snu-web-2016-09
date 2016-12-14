class Base:
    '클래스 버전 base 장식자를 구현'
    def __init__(self, base_fn):
        self.base_fn = base_fn

    def __call__(self, fn):
        def wrap(*args):
            return self.base_fn(fn(*args))
        return wrap

@Base(lambda i: i+10)
def mysum(*args):
    '불특정 다수의 Positional Arguments 를 모두 더합니다.'
    result = 0
    for i in args:
        result += i
    return result

if __name__ == '__main__':
    assert mysum(1, 2, 3) == 16
    assert mysum(*range(1, 1001)) == 500510
    print('PASS')
