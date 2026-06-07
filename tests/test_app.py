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


# ---------------------------------------------------------------------------
# Edge case tests — Large and small numbers
# ---------------------------------------------------------------------------

def test_add_large_numbers():
    assert add(1e10, 2e10) == pytest.approx(3e10)


def test_multiply_large_numbers():
    assert multiply(1e5, 1e5) == pytest.approx(1e10)


def test_divide_very_small_result():
    assert divide(1, 1e6) == pytest.approx(1e-6)


def test_subtract_large_negative():
    assert subtract(0, 1e10) == pytest.approx(-1e10)


# ---------------------------------------------------------------------------
# Edge case tests — Zero operations
# ---------------------------------------------------------------------------

def test_add_zero():
    assert add(0, 5) == 5


def test_subtract_zero():
    assert subtract(10, 0) == 10


def test_divide_zero_by_number():
    assert divide(0, 5) == 0


def test_add_zero_to_zero():
    assert add(0, 0) == 0


def test_multiply_zero_times_large_number():
    assert multiply(0, 1e10) == 0


# ---------------------------------------------------------------------------
# Edge case tests — Mixed int and float
# ---------------------------------------------------------------------------

def test_add_int_and_float():
    assert add(3, 2.5) == pytest.approx(5.5)


def test_subtract_float_and_int():
    assert subtract(10.5, 3) == pytest.approx(7.5)


def test_multiply_int_and_float():
    assert multiply(4, 2.5) == pytest.approx(10.0)


def test_divide_int_by_float():
    assert divide(5, 2.5) == pytest.approx(2.0)


# ---------------------------------------------------------------------------
# Edge case tests — Boolean inputs (Python treats bool as int)
# ---------------------------------------------------------------------------

def test_add_with_boolean_true():
    assert add(True, 1) == 2


def test_add_with_boolean_false():
    assert add(False, 5) == 5


def test_multiply_with_boolean():
    assert multiply(True, 10) == 10


# ---------------------------------------------------------------------------
# Additional error-handling tests — Other invalid types
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("fn", [add, subtract, multiply, divide])
def test_dict_input_raises(fn):
    with pytest.raises(InvalidInputError):
        fn({"a": 1}, 2)


@pytest.mark.parametrize("fn", [add, subtract, multiply, divide])
def test_tuple_input_raises(fn):
    with pytest.raises(InvalidInputError):
        fn((1, 2), 3)


@pytest.mark.parametrize("fn", [add, subtract, multiply, divide])
def test_set_input_raises(fn):
    with pytest.raises(InvalidInputError):
        fn({1, 2}, 3)


# ---------------------------------------------------------------------------
# Precision and floating-point tests
# ---------------------------------------------------------------------------

def test_divide_precision():
    """Test that divide maintains reasonable precision."""
    result = divide(1, 3)
    # 1/3 should be approximately 0.333...
    assert result == pytest.approx(0.3333333333, rel=1e-9)


def test_multiply_then_divide_round_trip():
    """Test that multiply followed by divide returns original value."""
    original = 7
    multiplied = multiply(original, 2.5)
    result = divide(multiplied, 2.5)
    assert result == pytest.approx(original)


def test_commutative_add():
    """Test that addition is commutative."""
    assert add(3, 5) == add(5, 3)


def test_commutative_multiply():
    """Test that multiplication is commutative."""
    assert multiply(4, 7) == multiply(7, 4)


# ---------------------------------------------------------------------------
# More comprehensive error message tests
# ---------------------------------------------------------------------------

def test_divide_by_zero_error_message_exact():
    """Verify exact error message for division by zero."""
    with pytest.raises(DivisionByZeroError) as exc_info:
        divide(42, 0)
    assert str(exc_info.value) == "Cannot divide by zero."


def test_invalid_input_error_mentions_none():
    """Verify error message when None is provided."""
    with pytest.raises(InvalidInputError, match="None"):
        add(None, 5)


def test_invalid_input_error_shows_type_info():
    """Verify error message shows the problematic types."""
    with pytest.raises(InvalidInputError, match="str"):
        multiply("hello", 2)


# ---------------------------------------------------------------------------
# Boundary tests for division
# ---------------------------------------------------------------------------

def test_divide_negative_by_positive():
    assert divide(-10, 2) == -5


def test_divide_positive_by_negative():
    assert divide(10, -2) == -5


def test_divide_negative_by_negative():
    assert divide(-10, -2) == 5


# ---------------------------------------------------------------------------
# Operations with floats very close to zero
# ---------------------------------------------------------------------------

def test_divide_by_very_small_number():
    """Test dividing by a very small but non-zero number."""
    result = divide(1, 1e-10)
    assert result == pytest.approx(1e10)


def test_subtract_very_close_numbers():
    """Test subtracting numbers that are very close to each other."""
    a = 1.0000001
    b = 1.0000000
    result = subtract(a, b)
    assert result > 0