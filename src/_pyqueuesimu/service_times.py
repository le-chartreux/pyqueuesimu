from _pyqueuesimu.time_to_next_event import generate_time_to_next_event


def generate_service_times(service_rate: float, number_of_clients: int) -> list[float]:
    """Generate for each client a service time, following an exponential law.

    Args:
        service_rate: average number of clients per time units that are served
        number_of_clients: number of clients to serve

    Returns: A list of service times, where result[i] is the service time of client i.
    """
    return [generate_time_to_next_event(service_rate) for _ in range(number_of_clients)]
