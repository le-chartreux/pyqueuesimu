import statistics


def get_average_service_time(service_times: list[float]) -> float:
    """Get the average service time from the service times.

    Args:
        service_times: list where service_times[i] is the service time of client i.
    """
    return statistics.mean(service_times)
