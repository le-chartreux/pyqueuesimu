import statistics


def get_waiting_times(
    arrival_times: list[float], departure_times: list[float], service_times: list[float]
) -> list[float]:
    """Compute the waiting times."""
    return [
        departure_time - arrival_time - service_time
        for arrival_time, departure_time, service_time in zip(
            arrival_times, departure_times, service_times, strict=True
        )
    ]


def get_average_waiting_time(waiting_times: list[float]) -> float:
    """Get the average waiting time from the waiting times."""
    return statistics.mean(waiting_times)
