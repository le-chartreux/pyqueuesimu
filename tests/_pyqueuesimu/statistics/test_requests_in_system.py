import pytest

from _pyqueuesimu.statistics.requests_in_system import get_average_number_of_requests_in_system


@pytest.mark.parametrize(
    ("arrival_times", "departure_times", "observation_duration", "expected_result"),
    [
        ([0.2, 1, 1.1, 1.2, 3, 5], [1.2, 1.21, 4, 4.01, 4.1, 6], 8, 1.13875)
    ]
)
def test_get_average_number_of_requests_in_system(arrival_times: list[float], departure_times: list[float], observation_duration: float, expected_result: float) -> None:
    assert get_average_number_of_requests_in_system(arrival_times, departure_times, observation_duration) == expected_result
