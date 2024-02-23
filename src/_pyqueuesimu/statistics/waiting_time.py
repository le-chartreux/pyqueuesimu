import statistics


def get_waiting_times(
    arrival_times: list[float], departure_times: list[float], service_times: list[float]
) -> list[float]:
    """Compute the waiting times.

    Args:
        arrival_times: list where arrival_times[i] is the moment where client i arrived.
        departure_times: list where departure_times[i] is the moment where client i left.
        service_times: list where service_times[i] is the service time of client i.

    Returns:
        A list of waiting times, where result[i] is the time wait by client i.
    """
    return [
        departure_time - arrival_time - service_time
        for arrival_time, departure_time, service_time in zip(
            arrival_times, departure_times, service_times, strict=True
        )
    ]


def get_average_waiting_time(waiting_times: list[float]) -> float:
    """Get the average waiting time from the waiting times.

    Args:
        waiting_times: list where waiting_times[i] is the time wait by client i.
    """
    return statistics.mean(waiting_times)
