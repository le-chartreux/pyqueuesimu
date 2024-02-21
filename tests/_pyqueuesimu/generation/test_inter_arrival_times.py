from unittest.mock import Mock, call, patch

import pytest

from _pyqueuesimu.generation.inter_arrival_times import generate_inter_arrival_times


@pytest.mark.parametrize(
    ("time_to_next_event", "observation_duration"),
    [(1, 100), (4.5, 100), (140.92, 100), (140.92, 200)],
)
@patch("_pyqueuesimu.generation.inter_arrival_times.generate_time_to_next_event")
def test_generate_inter_arrival_times(
    mock_generate_time_to_next_event: Mock,
    *,
    time_to_next_event: float,
    observation_duration: float,
) -> None:
    mock_generate_time_to_next_event.return_value = time_to_next_event
    number_of_events = int(observation_duration // time_to_next_event)
    expected_result = [time_to_next_event] * number_of_events
    result = generate_inter_arrival_times(1, observation_duration)
    assert result == expected_result
    mock_generate_time_to_next_event.assert_has_calls([call(1)] * number_of_events)


def test_generate_inter_arrival_times__sum_below_duration() -> None:
    # tested a lot of time to assert that it does not pass by luck
    for _ in range(100):
        result = generate_inter_arrival_times(1, 15)
        assert sum(result) < 15


@pytest.mark.parametrize(
    ("constant_rate", "observation_duration"),
    [(1, 1000), (0.1, 10000), (100, 10), (42.97, 50), (93.19021, 10), (32.914401, 100)],
)
def test_generate_inter_arrival_times__coherent_number_of_elements(
    *, constant_rate: float, observation_duration: float
) -> None:
    """It produces a number of events near constant_rate * observation_duration."""
    expected_len = constant_rate * observation_duration
    result = generate_inter_arrival_times(constant_rate, observation_duration)
    assert (expected_len * 0.9) < len(result) < (expected_len * 1.1)
