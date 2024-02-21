import statistics


def get_average_service_time(service_times: list[float]) -> float:
    """Get the average service time from the service times."""
    return statistics.mean(service_times)
