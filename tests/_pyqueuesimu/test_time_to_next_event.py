import math
from unittest.mock import Mock, patch

import pytest

from _pyqueuesimu.time_to_next_event import generate_time_to_next_event


@patch("_pyqueuesimu.time_to_next_event.random.random")
@pytest.mark.parametrize(
    ("random_return_value", "expected_result"), [(0.01, 4.6), (0.5, 0.69), (0.99, 0.01)]
)
def test_generate_time_to_next_event(
    mock_random: Mock,
    *,
    random_return_value: float,
    expected_result: float,
) -> None:
    mock_random.return_value = random_return_value
    assert math.isclose(generate_time_to_next_event(1), expected_result, abs_tol=0.01)
