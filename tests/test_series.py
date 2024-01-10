import pytest
from math_series.series import fibonacci, lucas, sum_series

def test_1():
    actual = fibonacci(1)
    expected = 0
    assert actual == expected
    
def test_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected
    
def test_four():
    actual = fibonacci(4)
    expected = 2
    assert actual == expected
    
def test_five():
    actual = fibonacci(5)
    expected = 3
    assert actual == expected
    
def test_lucas_two():
    actual = lucas(2)
    expected = 1
    assert actual == expected

def test_lucas_three():
    actual = lucas(3)
    expected = 3
    assert actual == expected

def test_lucas_four():
    actual = lucas(4)
    expected = 4
    assert actual == expected
    
def test_sum_series_fibonacci():
    n = 5
    actual = sum_series(n)
    expected = 5
    assert actual == expected

def test_sum_series_lucas():
    n = 5
    actual = sum_series(n, 2, 1)
    expected = 11
    assert actual == expected