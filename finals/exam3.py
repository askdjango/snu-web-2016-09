def base(base_fn):
    def wrap(fn):
        def inner(*args):
            return base_fn(fn(*args))
        return inner
    return wrap

@base(lambda i: i+10)
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
