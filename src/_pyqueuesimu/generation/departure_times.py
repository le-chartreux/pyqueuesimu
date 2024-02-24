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
    # same that with a limited buffer that can fit everything
    return get_departure_times_limited_buffer(
        arrival_times, service_times, len(arrival_times)
    )


def get_departure_times_limited_buffer(
    arrival_times: list[float], service_times: list[float], buffer_size: int
) -> list[float]:
    """Get the ordinated list of time departures with a limited buffer size.

    Args:
        arrival_times: ordinated list where result[i] is the moment where client i
            arrived.
        service_times: ordinated list where service_times[i] is the number of time units
            between the arrival of client i and its departure.
        buffer_size: size of the buffer. If the number of clients is greater than the
            buffer size + 1 (because of the client that is currently serviced), the
            next clients to arrive will be lost.

    Returns:
        An ordinated list where result[i] is the moment where client i left the system.
        If client i was lost, result[i] = -1

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
        number_of_clients = sum(
            1 for departure_time in departure_times if departure_time > arrival_time
        )
        if number_of_clients < buffer_size + 1:
            beginning_of_computation_time = max(arrival_time, previous_departure_time)
            departure_time = beginning_of_computation_time + service_time
            departure_times.append(departure_time)
            previous_departure_time = departure_time
        else:
            departure_times.append(-1)
    return departure_times
