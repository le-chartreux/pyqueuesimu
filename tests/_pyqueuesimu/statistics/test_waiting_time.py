import math

import pytest

from _pyqueuesimu.statistics.waiting_time import (
    get_average_waiting_time,
    get_waiting_times,
)


@pytest.mark.parametrize(
    ("arrival_times", "departure_times", "expected_result"),
    [([1, 1.5, 2, 3], [2, 2.1, 3, 3.4], [1, 0.6, 1, 0.4])],
)
def test_get_waiting_times(
    arrival_times: list[float],
    departure_times: list[float],
    expected_result: list[float],
) -> None:
    result = get_waiting_times(arrival_times, departure_times)
    assert all(
        math.isclose(elem_result, elem_expected_result)
        for elem_result, elem_expected_result in zip(
            result, expected_result, strict=True
        )
    )


@pytest.mark.parametrize(
    ("waiting_times", "expected_result"), [([1, 1, 1], 1), ([1, 2, 1, 4, 2.5], 2.1)]
)
def test_get_average_waiting_time(
    waiting_times: list[float], expected_result: float
) -> None:
    assert get_average_waiting_time(waiting_times) == expected_result
