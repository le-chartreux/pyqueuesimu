import pytest

from _pyqueuesimu.arrival_times import get_arrival_times


@pytest.mark.parametrize(
    ("time_between_arrivals", "expected_result"),
    [
        ([1, 1, 1, 1], [1, 2, 3, 4]),
        ([0.1, 2.1, 3.8, 0.4], [0.1, 2.2, 6, 6.4]),
        ([1], [1]),
    ],
)
def test_get_arrival_times_from_time_between_arrivals(
    *, time_between_arrivals: list[float], expected_result: list[float]
) -> None:
    result = get_arrival_times(time_between_arrivals)
    assert result == expected_result
