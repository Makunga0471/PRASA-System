# Unit tests for Calculator functions
# Covers:
# - Basic arithmetic operations
# - Edge cases (negative numbers, floats, zero)
# - Error handling (invalid inputs and division by zero)

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
# Additional tests for valid inputs (edge cases and numeric variations)
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
# Tests for division by zero handling and custom exception behavior
# ---------------------------------------------------------------------------

def test_divide_by_zero_raises():
    """Ensures division by zero raises DivisionByZeroError instead of returning a value."""
    with pytest.raises(DivisionByZeroError):
        divide(10, 0)


def test_divide_by_zero_is_calculator_error():
    """Checks that invalid input error message contains 'numeric' keyword."""
    with pytest.raises(CalculatorError):
        divide(1, 0)


def test_divide_by_zero_message():
    with pytest.raises(DivisionByZeroError, match="Cannot divide by zero"):
        divide(5, 0)


# ---------------------------------------------------------------------------
# Tests for invalid input validation (type safety checks)
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
# Tests verifying correct exception inheritance structure
# ---------------------------------------------------------------------------

def test_exception_hierarchy():
    """Verifies correct inheritance of custom exceptions from base CalculatorError."""
    assert issubclass(DivisionByZeroError, CalculatorError)
    assert issubclass(InvalidInputError, CalculatorError)
    assert issubclass(CalculatorError, Exception)