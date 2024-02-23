def get_incoming_throughput(
    arrivals: list[float], observation_duration: float
) -> float:
    """Compute the incoming throughput.

    Args:
        arrivals: list where arrivals[i] is the moment where client i arrived.
        observation_duration: how long the observation lasts.
    """
    return len(arrivals) / observation_duration


def get_outgoing_throughput(
    departures: list[float], observation_duration: float
) -> float:
    """Compute the outgoing throughput.

    Args:
        departures: list where departures[i] is the moment where client i left.
        observation_duration: how long the observation lasts.
    """
    return len(departures) / observation_duration
