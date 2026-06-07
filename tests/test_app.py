# Unit tests for Calculator functions
import pytest
from app import (
    add, subtract, multiply, divide, modulo,
    CalculatorError, DivisionByZeroError, InvalidInputError,
)

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 2) == 3

def test_multiply():
    assert multiply(4, 5) == 20

def test_divide():
    assert divide(10, 2) == 5

def test_add_floats():
    assert add(1.5, 2.5) == pytest.approx(4.0)

def test_subtract_negative_result():
    assert subtract(2, 5) == -3

def test_multiply_by_zero():
    assert multiply(7, 0) == 0

def test_divide_returns_float():
    assert divide(7, 2) == pytest.approx(3.5)

def test_add_negative_numbers():
    assert add(-3, -4) == -7

def test_multiply_negative_numbers():
    assert multiply(-3, 4) == -12

def test_divide_by_zero_raises():
    with pytest.raises(DivisionByZeroError):
        divide(10, 0)

def test_divide_by_zero_is_calculator_error():
    with pytest.raises(CalculatorError):
        divide(1, 0)

def test_divide_by_zero_message():
    with pytest.raises(DivisionByZeroError, match="Cannot divide by zero"):
        divide(5, 0)

@pytest.mark.parametrize("fn", [add, subtract, multiply, divide])
def test_none_first_arg_raises(fn):
    with pytest.raises(InvalidInputError):
        fn(None, 1)

@pytest.mark.parametrize("fn", [add, subtract, multiply, divide])
def test_none_second_arg_raises(fn):
    with pytest.raises(InvalidInputError):
        fn(1, None)

@pytest.mark.parametrize("fn", [add, subtract, multiply, divide])
def test_string_input_raises(fn):
    with pytest.raises(InvalidInputError):
        fn("two", 2)

@pytest.mark.parametrize("fn", [add, subtract, multiply, divide])
def test_list_input_raises(fn):
    with pytest.raises(InvalidInputError):
        fn([1, 2], 3)

def test_invalid_input_is_calculator_error():
    with pytest.raises(CalculatorError):
        add("x", 1)

def test_invalid_input_message_contains_type():
    with pytest.raises(InvalidInputError, match="numeric"):
        multiply("abc", 2)

def test_exception_hierarchy():
    assert issubclass(DivisionByZeroError, CalculatorError)
    assert issubclass(InvalidInputError, CalculatorError)
    assert issubclass(CalculatorError, Exception)


class TestModulo:
    def test_modulo_basic(self):
        assert modulo(10, 3) == 1

    def test_modulo_even_division(self):
        assert modulo(9, 3) == 0

    def test_modulo_floats(self):
        assert modulo(10.5, 3) == pytest.approx(1.5)

    def test_modulo_by_zero_raises(self):
        with pytest.raises(DivisionByZeroError):
            modulo(10, 0)

    def test_modulo_none_raises(self):
        with pytest.raises(InvalidInputError):
            modulo(None, 3)
