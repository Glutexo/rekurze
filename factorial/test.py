import pytest

from bez_rekurze import factorial as factorial_bez_rekurze
from s_rekurzi import factorial as factorial_s_rekurzi

parametrize_function = pytest.mark.parametrize(("factorial",), ((factorial_bez_rekurze,), (factorial_s_rekurzi,)))


@parametrize_function
def test_zero(factorial):
    assert factorial(0) == 1


test_data = [(1, 1), (2, 2), (3, 6), (4, 24), (5, 120), (10, 3628800)]


@parametrize_function
@pytest.mark.parametrize(("input", "result"), test_data)
def test_positive_integer(input, result, factorial):
    assert factorial(input) == result
