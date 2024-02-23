import pytest

from _pyqueuesimu.statistics.throughput import get_incoming_throughput, get_outgoing_throughput


@pytest.mark.parametrize(
    ("arrivals", "observation_duration", "expected_result"),
    [
        ([], 100, 0),
        ([1, 2, 18], 30, 0.1),
        ([0.4, 0.15, 1.54, 1.61, 1.89, 1.99], 2, 3)
    ]
)
def test_get_incoming_throughput(arrivals: list[float], observation_duration: float, expected_result: float) -> None:
    assert get_incoming_throughput(arrivals, observation_duration) == expected_result


@pytest.mark.parametrize(
    ("arrivals", "observation_duration", "expected_result"),
    [
        ([], 100, 0),
        ([1, 2, 18], 30, 0.1),
        ([0.4, 0.15, 1.54, 1.61, 1.89, 1.99], 2, 3)
    ]
)
def test_get_outgoing_throughput(arrivals: list[float], observation_duration: float, expected_result: float) -> None:
    assert get_outgoing_throughput(arrivals, observation_duration) == expected_result
