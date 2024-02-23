def get_incoming_throughput(arrivals: list[float], observation_duration: float) -> float:
    return len(arrivals) / observation_duration