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
    departure_times = []
    previous_departure_time = 0.0
    for arrival_time, service_time in zip(arrival_times, service_times, strict=True):
        beginning_of_computation_time = max(arrival_time, previous_departure_time)
        departure_time = beginning_of_computation_time + service_time
        departure_times.append(departure_time)
        previous_departure_time = departure_time
    return departure_times
