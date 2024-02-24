import pytest

from _pyqueuesimu.statistics.loss_rate import get_loss_rate


@pytest.mark.parametrize(
    ("departures", "expected_result"),
    [
        ([1, 2, None, 4, None, 14, 17, 20], 0.25),
        ([1, 2, 3, 4, 5, 14], 0),
        ([None, None, None], 1),
        ([], 0),
        ([1], 0),
        ([None], 1),
    ],
)
def test_get_loss_rate(
    *, departures: list[float | None], expected_result: float
) -> None:
    assert get_loss_rate(departures) == expected_result
