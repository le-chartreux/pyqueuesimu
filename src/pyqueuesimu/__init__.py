"""Public package of pyqueuesimu."""

from _pyqueuesimu.generation.arrival_times import get_arrival_times
from _pyqueuesimu.generation.departure_times import get_departure_times
from _pyqueuesimu.generation.inter_arrival_times import generate_inter_arrival_times
from _pyqueuesimu.generation.service_times import generate_service_times
from _pyqueuesimu.statistics.clients_in_system import (
    get_average_number_of_clients_in_system,
    get_clients_in_system_times,
)
from _pyqueuesimu.statistics.service_time import get_average_service_time
from _pyqueuesimu.statistics.waiting_time import (
    get_average_waiting_time,
    get_waiting_times,
)

__all__ = [
    "get_arrival_times",
    "get_departure_times",
    "generate_inter_arrival_times",
    "generate_service_times",
    "get_waiting_times",
    "get_average_waiting_time",
    "get_average_service_time",
    "get_average_number_of_clients_in_system",
    "get_clients_in_system_times",
]
