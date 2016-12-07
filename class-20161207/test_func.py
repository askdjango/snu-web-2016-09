# test_func.py
from func import func, base_add

def test_func():
    assert func(1) == 3

def test_base_add1():
    assert base_add(1, 2) == 113

def test_base_add2():
    assert base_add(10, 2) == 122

