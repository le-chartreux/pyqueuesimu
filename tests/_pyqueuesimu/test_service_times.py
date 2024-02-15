from unittest.mock import Mock, call, patch

from _pyqueuesimu.service_times import generate_service_times


@patch("_pyqueuesimu.service_times.generate_time_to_next_event")
def test_generate_service_times(mock_generate_time_to_next_event: Mock) -> None:
    mock_generate_time_to_next_event.side_effect = range(100)
    assert generate_service_times(10, 8) == list(range(8))
    mock_generate_time_to_next_event.assert_has_calls([call(10)] * 8)
