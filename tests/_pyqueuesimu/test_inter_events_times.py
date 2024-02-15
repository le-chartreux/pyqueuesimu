import math
from unittest.mock import Mock, call, patch

import pytest

from _pyqueuesimu.inter_events_times import (
    _generate_time_to_next_event,
    generate_inter_events_times_exponential,
)


@patch("_pyqueuesimu.inter_events_times._generate_time_to_next_event")
def test_generate_inter_events_times_exponential(
    mock__generate_time_to_next_event: Mock,
) -> None:
    mock__generate_time_to_next_event.return_value = 1.1
    expected_result = [mock__generate_time_to_next_event.return_value] * 4
    result = generate_inter_events_times_exponential(1, 5)
    assert result == expected_result
    mock__generate_time_to_next_event.assert_has_calls([call(1)] * 4)


def test_generate_inter_events_times_exponential__sum_below_duration() -> None:
    # tested a lot of time to assert that it does not pass by luck
    for _ in range(100):
        result = generate_inter_events_times_exponential(1, 15)
        assert sum(result) < 15


@pytest.mark.parametrize(
    ("constant_rate", "observation_duration"),
    [(1, 1000), (0.1, 10000), (100, 10), (42.97, 50), (93.19021, 10), (32.914401, 100)]
)
def test_generate_inter_events_times_exponential__coherent_number_of_elements(
    *, constant_rate: float, observation_duration: float
) -> None:
    """It produces a number of events near constant_rate * observation_duration."""
    expected_len = constant_rate * observation_duration
    result = generate_inter_events_times_exponential(constant_rate, observation_duration)
    assert (expected_len * 0.9) < len(result) < (expected_len * 1.1)


@patch("_pyqueuesimu.inter_events_times.random.random")
@pytest.mark.parametrize(
    ("random_return_value", "expected_result"), [(0.01, 4.6), (0.5, 0.69), (0.99, 0.01)]
)
def test__generate_time_to_next_event(
    mock_random: Mock,
    *,
    random_return_value: float,
    expected_result: float,
) -> None:
    mock_random.return_value = random_return_value
    assert math.isclose(_generate_time_to_next_event(1), expected_result, abs_tol=0.01)
