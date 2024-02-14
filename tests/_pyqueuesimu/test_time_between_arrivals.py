import math
from unittest.mock import Mock, call, patch

import pytest

from _pyqueuesimu.time_between_arrivals import (
    _generate_time_to_next_arrival,
    generate_times_between_arrivals,
)


@patch("_pyqueuesimu.time_between_arrivals._generate_time_to_next_arrival")
def test_generate_times_between_arrivals(
    mock__generate_time_to_next_arrival: Mock,
) -> None:
    mock__generate_time_to_next_arrival.return_value = 1.1
    expected_result = [mock__generate_time_to_next_arrival.return_value] * 4
    result = generate_times_between_arrivals(1, 5)
    assert result == expected_result
    mock__generate_time_to_next_arrival.assert_has_calls([call(1)] * 4)


def test_generate_times_between_arrivals__sum_below_duration() -> None:
    # tested a lot of time to assert that it does not pass by luck
    for _ in range(100):
        result = generate_times_between_arrivals(1, 15)
        assert sum(result) < 15


@patch("_pyqueuesimu.time_between_arrivals.random.random")
@pytest.mark.parametrize(
    ("random_return_value", "expected_result"), [(0.01, 4.6), (0.5, 0.69), (0.99, 0.01)]
)
def test__generate_time_to_next_arrival(
    mock_random: Mock,
    *,
    random_return_value: float,
    expected_result: float,
) -> None:
    mock_random.return_value = random_return_value
    assert math.isclose(
        _generate_time_to_next_arrival(1), expected_result, abs_tol=0.01
    )
