import pytest
from app import (
    add, subtract, multiply, divide,
    CalculatorError, DivisionByZeroError, InvalidInputError,
)


# ---------------------------------------------------------------------------
# Original happy-path tests (unchanged)
# ---------------------------------------------------------------------------

def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 2) == 3


def test_multiply():
    assert multiply(4, 5) == 20


def test_divide():
    assert divide(10, 2) == 5


# ---------------------------------------------------------------------------
# Additional happy-path tests
# ---------------------------------------------------------------------------

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


# ---------------------------------------------------------------------------
# Error-handling tests — DivisionByZeroError
# ---------------------------------------------------------------------------

def test_divide_by_zero_raises():
    """divide(x, 0) must raise DivisionByZeroError, not return a string."""
    with pytest.raises(DivisionByZeroError):
        divide(10, 0)


def test_divide_by_zero_is_calculator_error():
    """DivisionByZeroError must be a subclass of CalculatorError."""
    with pytest.raises(CalculatorError):
        divide(1, 0)


def test_divide_by_zero_message():
    with pytest.raises(DivisionByZeroError, match="Cannot divide by zero"):
        divide(5, 0)


# ---------------------------------------------------------------------------
# Error-handling tests — InvalidInputError
# ---------------------------------------------------------------------------

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
    """InvalidInputError must be a subclass of CalculatorError."""
    with pytest.raises(CalculatorError):
        add("x", 1)


def test_invalid_input_message_contains_type():
    with pytest.raises(InvalidInputError, match="numeric"):
        multiply("abc", 2)


# ---------------------------------------------------------------------------
# Exception hierarchy
# ---------------------------------------------------------------------------

def test_exception_hierarchy():
    assert issubclass(DivisionByZeroError, CalculatorError)
    assert issubclass(InvalidInputError, CalculatorError)
    assert issubclass(CalculatorError, Exception)