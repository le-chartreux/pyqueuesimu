import math

import pytest

from _pyqueuesimu.departure_times import get_departure_times


@pytest.mark.parametrize(
    ("arrival_times", "service_times", "expected_result"),
    [
        ([1] * 4, [1] * 4, [2] * 4),
        ([0.1, 2.1, 3.8, 0.4], [1.1, 0.7, 2.1, 0.01], [1.2, 2.8, 5.9, 0.41]),
        ([], [], []),
    ],
)
def test_get_departure_times(
    *, arrival_times: list[float], service_times: list[float], expected_result: list[float]
) -> None:
    result = get_departure_times(arrival_times, service_times)
    assert all(
        math.isclose(elem_result, elem_expected_result)
        for elem_result, elem_expected_result in zip(result, expected_result)
    )


def test_get_departure_times__raise_when_size_differs() -> None:
    with pytest.raises(ValueError) as error:
        get_departure_times([], [1])
    assert str(error.value) == "len(arrival_times) != len(service_times): 0 != 1"

    with pytest.raises(ValueError) as error:
        get_departure_times([5, 2, 7], [1])
    assert str(error.value) == "len(arrival_times) != len(service_times): 3 != 1"
