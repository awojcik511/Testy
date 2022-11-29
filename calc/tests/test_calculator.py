from calc.calculator import Calculator
import pytest


def test_add_two():
    calculator = Calculator()
    result = calculator.add(1,1)
    assert result == 2

def test_add_three():
    calculator = Calculator()
    result = calculator.add(1,1,1)
    assert result == 3

def test_add_random():
    calculator = Calculator()
    result = calculator.add(1,2,3,4,5)
    assert result == 15

def test_substract():
    calculator = Calculator()
    result = calculator.sub(2,1)
    assert result == 1 

def test_multiply_two():
    calculator = Calculator()
    result = calculator.multi(3,4)
    assert result == 12

def test_multiply_random():
    calculator = Calculator()
    result = calculator.multi(3,4,2,1)
    assert result == 24

@pytest.mark.parametrize("a, b, c", [(15,2, 7.5), (0, 4, 0)])
def test_division(a, b, c):
    calculator = Calculator()
    result = calculator.division(a, b)
    assert result == c

def test_division_by_zero():
    calculator = Calculator()
    result = calculator.division(4,0)
    assert result == float("inf")

def test_multiply_by_zero():
    calculator = Calculator()
    with pytest.raises(ValueError):
        calculator.multi(4, 0)

def test_average():
    calculator = Calculator()
    result = calculator.average([3, 4, 5])
    assert result == 4

def test_average_over():
    calculator = Calculator()
    result = calculator.average([3, 4, 5, 91], 90)
    assert result == 4

def test_average_under():
    calculator = Calculator()
    result = calculator.average([3, 4, 5, 91], None, 10)
    assert result == 91

@pytest.mark.parametrize("number_list, ut, lt, avg_result", [([3, 4, 5, 11, 92], 91, 10, 11), ([3, 4, 5, 11, 92], 0, 0, 0)])
def test_average_under_over(number_list, ut, lt, avg_result):
    calculator = Calculator()
    result = calculator.average(number_list, ut, lt)
    assert result == avg_result