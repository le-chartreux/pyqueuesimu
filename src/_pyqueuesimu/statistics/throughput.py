def get_incoming_throughput(
    arrivals: list[float], observation_duration: float
) -> float:
    """Compute the incoming throughput."""
    return len(arrivals) / observation_duration


def get_outgoing_throughput(
    departures: list[float], observation_duration: float
) -> float:
    """Compute the outgoing throughput."""
    return len(departures) / observation_duration
