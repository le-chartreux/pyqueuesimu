def get_departure_times(
    arrival_times: list[float],
    service_times: list[float],
) -> list[float]:
    """Get the ordinated list of time departures.

    Args:
        arrival_times: ordinated list where result[i] is the moment where client i
            arrived.
        service_times: ordinated list where service_times[i] is the number of time units
            between the arrival of client i and its departure.

    Returns:
        An ordinated list where result[i] is the moment where client i left the system.

    Raises:
        ValueError: When len(arrival_times) != len(service_times)
    """
    if len(arrival_times) != len(service_times):
        error_message = (
            "len(arrival_times) != len(service_times): "
            f"{len(arrival_times)} != {len(service_times)}"
        )
        raise ValueError(error_message)
    # todo check with the teacher about the max that is in the given algorithm
    return [
        arrival_time + service_time
        for arrival_time, service_time in zip(arrival_times, service_times)
    ]
