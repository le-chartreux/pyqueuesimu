import pytest

from _pyqueuesimu.statistics.service_time import get_average_service_time


@pytest.mark.parametrize(
    ("service_times", "expected_result"), [([1, 1, 1], 1), ([1, 2, 1, 4, 2.5], 2.1)]
)
def test_get_average_service_time(
    service_times: list[float], expected_result: float
) -> None:
    assert get_average_service_time(service_times) == expected_result
