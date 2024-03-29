import math
import re

import pytest

from _pyqueuesimu.generation.departure_times import (
    get_departure_times,
    get_departure_times_limited_buffer,
)


@pytest.mark.parametrize(
    ("arrival_times", "service_times", "expected_result"),
    [
        ([1] * 4, [1] * 4, [2, 3, 4, 5]),
        ([0.1, 2.1, 3.8, 3.9], [1.1, 0.7, 2.1, 0.01], [1.2, 2.8, 5.9, 5.91]),
        ([], [], []),
    ],
)
def test_get_departure_times(
    *,
    arrival_times: list[float],
    service_times: list[float],
    expected_result: list[float],
) -> None:
    result = get_departure_times(arrival_times, service_times)
    assert all(
        math.isclose(elem_result, elem_expected_result)
        for elem_result, elem_expected_result in zip(
            result, expected_result, strict=True
        )
    )


@pytest.mark.parametrize(
    ("arrival_times", "service_times", "expected_error_message"),
    [
        ([], [1], "len(arrival_times) != len(service_times): 0 != 1"),
        ([5, 2, 7], [1], "len(arrival_times) != len(service_times): 3 != 1"),
    ],
)
def test_get_departure_times__raise_when_size_differs(
    arrival_times: list[float], service_times: list[float], expected_error_message: str
) -> None:
    with pytest.raises(ValueError, match=re.escape(expected_error_message)):
        get_departure_times(arrival_times, service_times)


@pytest.mark.parametrize(
    ("arrival_times", "service_times", "buffer_size", "expected_result"),
    [
        ([1] * 4, [1] * 4, 10, [2, 3, 4, 5]),
        ([1] * 4, [1] * 4, 1, [2, 3, None, None]),
        ([1] * 4, [1] * 4, 2, [2, 3, 4, None]),
        ([0.1, 2.1, 3.8, 3.9], [1.1, 0.7, 2.1, 0.01], 1, [1.2, 2.8, 5.9, 5.91]),
        ([0.1, 2.1, 3.8, 3.9], [1.1, 0.7, 2.1, 0.01], 0, [1.2, 2.8, 5.9, None]),
        ([0.1, 1, 3.8, 3.9, 6], [1.1, 0.7, 2.1, 0.01, 2], 0, [1.2, None, 5.9, None, 8]),
        ([1, 2, 3, 4, 5, 6], [5, 4, 5, 7, 1, 2], 2, [6, 10, 15, None, None, 17]),
        ([], [], 9, []),
    ],
)
def test_get_departure_times_limited_buffer(
    *,
    arrival_times: list[float],
    service_times: list[float],
    buffer_size: int,
    expected_result: list[float],
) -> None:
    result = get_departure_times_limited_buffer(
        arrival_times, service_times, buffer_size
    )
    assert all(
        elem_result is elem_expected_result
        or math.isclose(elem_result, elem_expected_result)
        for elem_result, elem_expected_result in zip(
            result, expected_result, strict=True
        )
    )


@pytest.mark.parametrize(
    ("arrival_times", "service_times", "expected_error_message"),
    [
        ([], [1], "len(arrival_times) != len(service_times): 0 != 1"),
        ([5, 2, 7], [1], "len(arrival_times) != len(service_times): 3 != 1"),
    ],
)
def test_get_departure_times_limited_buffer__raise_when_size_differs(
    arrival_times: list[float], service_times: list[float], expected_error_message: str
) -> None:
    with pytest.raises(ValueError, match=re.escape(expected_error_message)):
        get_departure_times_limited_buffer(arrival_times, service_times, 100)
