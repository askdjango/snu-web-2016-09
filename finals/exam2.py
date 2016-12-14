class GoodMemoryCalculator:
    def __init__(self):
        self.history = []

    def __call__(self, x, y, fn):
        result = fn(x, y)
        self.history.append(result)
        return result

if __name__ == '__main__':
    calculator = GoodMemoryCalculator()
    assert calculator(1, 2, lambda x, y: x+y) == 3
    assert calculator(1, 10, lambda x, y: x*y) == 10
    assert calculator(100, 10, lambda x, y: x//y) == 10
    assert calculator.history == [3, 10, 10]
    print('PASS')
