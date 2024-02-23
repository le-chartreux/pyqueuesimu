import math

import pytest

from _pyqueuesimu.statistics.clients import (
    get_average_number_of_clients,
    get_cumulated_time_for_each_number_of_clients,
    get_server_occupancy_rate,
)


@pytest.mark.parametrize(
    ("clients_in_system_times", "expected_result"),
    [
        ([1], 0),
        ([0, 1], 1),
        ([0, 1, 2, 510], 1),
        ([1, 1], 0.5),
        ([1, 1, 2, 1], 0.8),
    ],
)
def test_get_server_occupancy_rate(
    clients_in_system_times: list[float],
    expected_result: float,
) -> None:
    assert get_server_occupancy_rate(clients_in_system_times) == expected_result


@pytest.mark.parametrize(
    ("clients_in_system_times", "expected_result"),
    [
        ([1], 0),
        ([0, 1], 1),
        ([1, 1], 0.5),
        ([1, 1, 2, 1], 1.6),
    ],
)
def test_get_average_number_of_clients_in_system(
    clients_in_system_times: list[float], expected_result: float
) -> None:
    assert get_average_number_of_clients(clients_in_system_times) == expected_result


@pytest.mark.parametrize(
    ("arrival_times", "departure_times", "observation_duration", "expected_result"),
    [
        (
            [0.2, 1, 1.1, 1.2, 3, 5],
            [1.2, 1.21, 4, 4.01, 4.1, 6],
            8,
            [3.1, 1.89, 1.9, 1.11],
        ),
        ([], [], 10, [10]),
        ([], [], 0, [0]),
    ],
)
def test_get_clients_in_system_times(
    arrival_times: list[float],
    departure_times: list[float],
    observation_duration: float,
    expected_result: list[float],
) -> None:
    result = get_cumulated_time_for_each_number_of_clients(
        arrival_times, departure_times, observation_duration
    )
    assert all(
        math.isclose(elem_result, elem_expected_result)
        for elem_result, elem_expected_result in zip(
            result, expected_result, strict=True
        )
    )
