def get_arrival_times(
    time_between_arrivals: list[float],
) -> list[float]:
    """Get the ordinated list of time arrivals from the time between arrivals.

    Args:
        time_between_arrivals: ordinated list where time_between_arrivals[i] is the
            number of time units between the arrival of client i-1 and client i.
            time_between_arrivals[0] is the number of time units before the arrival of
            the first client.

    Returns:
        An ordinated list where result[i] is the moment where client i arrived.
    """
    return [
        sum(time_between_arrivals[: i + 1]) for i in range(len(time_between_arrivals))
    ]
