import pytest
from src.report_median_coffee import calculate_median


@pytest.mark.parametrize(
    "value, expectation",
    [
        ([10, 20, 30], 20),
        ([10, 20], 15)
    ]

)
def test_calculate_median_basic(value, expectation):
    assert calculate_median(value) == expectation


def test_calculate_median_single_value():
    assert calculate_median([20]) == 20


def test_calculate_median_empty():
    assert calculate_median([]) == 0.0
