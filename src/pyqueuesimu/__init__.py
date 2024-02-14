"""Public package of pyqueuesimu."""

from _pyqueuesimu.arrival_times import get_arrival_times_from_time_between_arrivals
from _pyqueuesimu.time_between_arrivals import generate_times_between_arrivals

__all__ = [
    "generate_times_between_arrivals",
    "get_arrival_times_from_time_between_arrivals",
]
